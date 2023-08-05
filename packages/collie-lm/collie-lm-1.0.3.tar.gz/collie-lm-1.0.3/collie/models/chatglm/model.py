import os
import gc
import json

import torch
from torch import Tensor, nn
import torch.nn.functional as F
import torch.distributed as dist
import torch.nn.init as init
from torch.nn.modules.module import Module
import torch.utils.checkpoint

from deepspeed.pipe import LayerSpec, TiedLayerSpec

from megatron.core import tensor_parallel
from megatron.core import parallel_state

import math
from einops import rearrange

try:
    from flash_attn.flash_attention import FlashAttention
except ModuleNotFoundError:
    FlashAttention = None

from collie.log.logger import logger
from collie.config import CollieConfig
from collie.models.base import CollieModelForCausalLM
from collie.driver.io import IODriver
from collie.module import ColumnParallelLinearWithoutBias, RowParallelLinearWithoutBias, ColumnParallelLMHead
from collie.utils import progress, env, dict_as_params, concat_tensor

from typing import Any, Union, Optional
from collections import OrderedDict
from transformers.modeling_utils import dtype_byte_size
from transformers.modeling_utils import PretrainedConfig
from transformers.modeling_outputs import CausalLMOutputWithPast

# class RotaryPositionEmbedding(nn.Module):
#     def __init__(self, head_dim: int) -> None:
#         super().__init__()
#         inv_freq = 1.0 / (10000.0 ** (
#             torch.arange(0, head_dim, 2)[: (head_dim // 2)].float() / head_dim))
#         self.register_buffer('inv_freq', inv_freq)

#     def forward(self,
#                 query: torch.Tensor,
#                 key: torch.Tensor,
#                 seq_len: int,
#                 start_pos: int = 0):
#         t = query.dtype
#         query = torch.view_as_complex(
#             query.float().reshape(*query.shape[:-1], -1, 2))
#         key = torch.view_as_complex(
#             key.float().reshape(*key.shape[:-1], -1, 2))
#         freqs = torch.outer(torch.arange(
#             (2 ** 16) * 2, device=self.inv_freq.device), self.inv_freq).float()
#         freqs_cis = torch.polar(torch.ones_like(freqs), freqs)[
#             start_pos: start_pos + seq_len]
#         print(freqs_cis.shape)
#         freqs_cis = torch.cat([freqs_cis, freqs_cis], dim=-1)
#         shape = [d if i == 1 or i == query.ndim -
#                  1 else 1 for i, d in enumerate(query.shape)]
#         freqs_cis = freqs_cis.view(*shape)
#         query = torch.view_as_real(query * freqs_cis).flatten(3)
#         key = torch.view_as_real(key * freqs_cis).flatten(3)
#         return query.type(t), key.type(t)
    
    
class RotaryEmbedding(torch.nn.Module):
    def __init__(self, dim, base=10000, precision=torch.half, learnable=False):
        super().__init__()
        inv_freq = 1. / (base ** (torch.arange(0, dim, 2).float() / dim))
        inv_freq = inv_freq.half()
        self.learnable = learnable
        if learnable:
            self.inv_freq = torch.nn.Parameter(inv_freq)
            self.max_seq_len_cached = None
        else:
            self.register_buffer('inv_freq', inv_freq)
            self.max_seq_len_cached = None
            self.cos_cached = None
            self.sin_cached = None
        self.precision = precision

    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys,
                              error_msgs):
        pass

    def forward(self, x, seq_dim=1, seq_len=None):
        if seq_len is None:
            seq_len = x.shape[seq_dim]
        if self.max_seq_len_cached is None or (seq_len > self.max_seq_len_cached):
            self.max_seq_len_cached = None if self.learnable else seq_len
            t = torch.arange(seq_len, device=x.device, dtype=self.inv_freq.dtype)
            freqs = torch.einsum('i,j->ij', t, self.inv_freq)
            # Different from paper, but it uses a different permutation in order to obtain the same calculation
            emb = torch.cat((freqs, freqs), dim=-1).to(x.device)
            if self.precision == torch.bfloat16:
                emb = emb.float()

            # [sx, 1 (b * np), hn]
            cos_cached = emb.cos()[:, None, :]
            sin_cached = emb.sin()[:, None, :]
            if self.precision == torch.bfloat16:
                cos_cached = cos_cached.bfloat16()
                sin_cached = sin_cached.bfloat16()
            if self.learnable:
                return cos_cached, sin_cached
            self.cos_cached, self.sin_cached = cos_cached, sin_cached
        return self.cos_cached[:seq_len, ...], self.sin_cached[:seq_len, ...]

    def _apply(self, fn):
        if self.cos_cached is not None:
            self.cos_cached = fn(self.cos_cached)
        if self.sin_cached is not None:
            self.sin_cached = fn(self.sin_cached)
        return super()._apply(fn)


def rotate_half(x):
    x1, x2 = x[..., :x.shape[-1] // 2], x[..., x.shape[-1] // 2:]
    return torch.cat((-x2, x1), dim=x1.ndim - 1)  # dim=-1 triggers a bug in earlier torch versions


@torch.jit.script
def apply_rotary_pos_emb_index(q, k, cos, sin, position_id):
    # position_id: [sq, b], q, k: [sq, b, np, hn], cos: [sq, 1, hn] -> [sq, b, 1, hn]
    cos, sin = F.embedding(position_id, cos.squeeze(1)).unsqueeze(2), \
        F.embedding(position_id, sin.squeeze(1)).unsqueeze(2)
    q, k = (q * cos) + (rotate_half(q) * sin), (k * cos) + (rotate_half(k) * sin)
    return q, k


class ChatGLMLayer(nn.Module):
    def __init__(self, config: CollieConfig, layer_id: int) -> None:
        super().__init__()
        self.config = config
        self.attention = nn.ModuleDict(
            {
                "query_key_value": ColumnParallelLinearWithoutBias(
                    config.hidden_size,
                    config.hidden_size * 3,
                    gather_output=False,
                    init_method=lambda x: x
                ),
                "dense": RowParallelLinearWithoutBias(
                    config.hidden_size,
                    config.hidden_size,
                    input_is_parallel=True,
                    init_method=lambda x: x
                ),
                "rotary_emb": RotaryEmbedding(
                    self.config.hidden_size // (self.config.num_attention_heads * 2))
            }
        )
        self.input_layernorm = nn.LayerNorm(
            config.hidden_size,
            eps=config.layernorm_epsilon
        )
        self.mlp = nn.ModuleDict({
            "dense_h_to_4h": ColumnParallelLinearWithoutBias(
                config.hidden_size,
                config.inner_hidden_size,
                gather_output=False,
                init_method=lambda x: x
            ),
            "dense_4h_to_h": RowParallelLinearWithoutBias(
                config.inner_hidden_size,
                config.hidden_size,
                input_is_parallel=True,
                init_method=lambda x: x
            )
        })
        self.post_attention_layernorm = nn.LayerNorm(
            config.hidden_size,
            eps=config.layernorm_epsilon
        )
        self.alpha = (2 * self.config.num_layers) ** 0.5
        self.layer_id = layer_id
        # 务必保持变量名一致
        self.use_cache = False
        self.past_key_values = None
        self.hidden_states = None
        
    def get_masks(self, input_ids, device):
        batch_size, seq_length = input_ids.shape
        context_lengths = [seq.tolist().index(self.config.bos_token_id) for seq in input_ids]
        attention_mask = torch.full((batch_size, seq_length, seq_length), float("-inf"))
        attention_mask = torch.triu(attention_mask, diagonal=1).to(device)
        for i, context_length in enumerate(context_lengths):
            attention_mask[i, :, :context_length] = 0.
        attention_mask.unsqueeze_(1)
        return attention_mask
        

    def _forward(self, hidden_states: torch.Tensor, input_ids: torch.Tensor, position_ids: torch.Tensor, attention_mask: Optional[torch.Tensor]=None):
        if attention_mask is None:
            attention_mask = torch.ones_like(input_ids)
        if not self.training:
            self.hidden_states = hidden_states
        else:
            self.hidden_states = None
        assert hidden_states.ndim == 3, f"hidden_states.shape must be (B, N, H), but got {hidden_states.shape}"
        batch_size, seq_len, _ = hidden_states.shape
        head_dim = self.config.hidden_size // self.config.num_attention_heads
        hidden_states = hidden_states.permute(1, 0, 2).contiguous() # [N, B, H]
        hidden_states = self.input_layernorm(hidden_states)
        query_key_value = self.attention["query_key_value"](hidden_states)
        query_key_value = rearrange(query_key_value, "b n (h d) -> b n h d", d=head_dim * 3)
        query, key, value = torch.chunk(query_key_value, 3, dim=-1)
        if not self.training and self.past_key_values is not None and self.use_cache:
            start_pos = self.past_key_values[0].shape[1]
            query = torch.cat([self.past_key_values[0], query], dim=1)
            key = torch.cat([self.past_key_values[0], key], dim=1)
            value = torch.cat([self.past_key_values[1], value], dim=1)
            self.past_key_values = [key, value]
        else:
            self.past_key_values = None
            start_pos = 0
        query1, query2 = query.chunk(2, dim=-1)
        key1, key2 = key.chunk(2, dim=-1)
        cos, sin = self.attention["rotary_emb"](query1, seq_len=position_ids.max() + 1)
        _position_ids, _block_position_ids = position_ids[:, 0, :].transpose(0, 1).contiguous(), \
            position_ids[:, 1, :].transpose(0, 1).contiguous()
        query1, key1 = apply_rotary_pos_emb_index(query1, key1, cos, sin, _position_ids)
        query2, key2 = apply_rotary_pos_emb_index(query2, key2, cos, sin, _block_position_ids)
        query = torch.concat([query1, query2], dim=(query1.ndim - 1))
        key = torch.concat([key1, key2], dim=(key1.ndim - 1))
        
        # if self.config.use_flash:
        if False: # TODO: flash attention not work for chatglm
            assert FlashAttention is not None, \
                "Detected flash_attn is not installed. See https://github.com/HazyResearch/flash-attention"
            qkv = torch.stack([query, key, value], dim=2)
            qkv = qkv.permute(1, 0, 2, 3, 4).contiguous()
            output, _ = FlashAttention()(qkv, causal=True)
            output = rearrange(output, "b n h d -> b n (h d)")
            output = F.dropout(output, p=self.config.dropout,
                               training=self.training)
        else:
            query = query / (math.sqrt(self.config.hidden_size // self.config.num_attention_heads) * float(self.layer_id + 1))
            query, key, value = query.permute(1, 2, 0, 3), key.permute(
                1, 2, 0, 3), value.permute(1, 2, 0, 3)
            attention_score = torch.matmul(query, key.transpose(
                2, 3))
            if seq_len + start_pos > 1:
                mask = self.get_masks(input_ids, hidden_states.device)
                attention_score = attention_score + mask
            attention_score = attention_score * float(self.layer_id + 1)
            key_padding_mask = (1.0 - attention_mask.unsqueeze(1).unsqueeze(2)) * torch.finfo(
                attention_score.dtype).min
            attention_score = F.softmax(
                attention_score + key_padding_mask, dim=-1).type_as(value)
            output = torch.matmul(attention_score, value)
            output = output.transpose(1, 2).contiguous().view(
                batch_size, seq_len + start_pos, -1)
            output = F.dropout(output, p=self.config.dropout,
                               training=self.training)
        output = output[:, start_pos:, :]
        hidden_states = hidden_states.permute(1, 0, 2) * self.alpha + self.attention["dense"](output)
        hidden_states = self.post_attention_layernorm(hidden_states)
        hidden_states = hidden_states * self.alpha + F.dropout(self.mlp["dense_4h_to_h"](F.gelu(self.mlp["dense_h_to_4h"](hidden_states))), p=self.config.dropout, training=self.training)
        return hidden_states

    def forward(self, inputs: dict):
        if self.config.checkpointing and self.training:
            inputs["hidden_states"] = torch.utils.checkpoint.checkpoint(
                self._forward,
                inputs["hidden_states"],
                inputs["input_ids"],
                inputs["position_ids"],
                inputs.get("attention_mask")
            )
        else:
            inputs["hidden_states"] = self._forward(
                hidden_states=inputs["hidden_states"],
                input_ids=inputs["input_ids"],
                position_ids=inputs["position_ids"],
                attention_mask=inputs.get("attention_mask"))
        return inputs


class ChatGLMForCausalLM(CollieModelForCausalLM):
    def __init__(self, config: CollieConfig) -> None:
        super().__init__(config)
        self.word_embeddings = self._get_word_embedding_with_position_ids_cls(config)(
            self.config.vocab_size,
            self.config.hidden_size
        )
        self.layers = nn.Sequential(
            *[ChatGLMLayer(self.config, i) for i in range(self.config.num_layers)])
        self.final_layernorm = nn.LayerNorm(
            self.config.hidden_size,
            eps=self.config.layernorm_epsilon
        )
        self.lm_head = ColumnParallelLinearWithoutBias(
            self.config.hidden_size,
            self.config.vocab_size,
            bias=False
        )
        # GenerationMixin 需要的额外参数
        self.config.is_decoder=True
        self.main_input_name = "input_ids"

    def forward(self, input_ids: torch.Tensor, **kwargs):
        attention_mask = kwargs.get("attention_mask", None)
        past_key_values=self._get_past_key_values(self.layers)
        if past_key_values is not None and not self.training:
            input_ids = input_ids[:, -1:]
        assert input_ids.ndim == 2, f"input_ids.shape must be (B, N), but got {input_ids.shape}"
        inputs = dict(zip(["hidden_states", "input_ids", "position_ids"], self.word_embeddings(input_ids)))
        if attention_mask is not None:
            inputs["attention_mask"] = attention_mask
        all_hidden_states = ()
        for layer in self.layers:
            all_hidden_states += (inputs["hidden_states"],)
            inputs = layer(inputs)
        inputs["hidden_states"] = self.final_layernorm(inputs["hidden_states"])
        logits = self.lm_head(inputs["hidden_states"])

        return CausalLMOutputWithPast(
            loss=None,
            logits=logits,
            past_key_values=self._get_past_key_values(self.layers),
            hidden_states=all_hidden_states,
            attentions=None
        )
        
    @staticmethod
    def _get_position_ids(config, input_ids: torch.Tensor, past_position_id: Optional[torch.Tensor]):
        if past_position_id is not None:
            return torch.cat((past_position_id, 
                              torch.stack((past_position_id[:, 0, -1].unsqueeze(-1), 
                                           past_position_id[:, 1, -1].unsqueeze(-1) + 1), dim=1)), dim=2)
        MASK, gMASK = config.mask_token_id, config.gmask_token_id
        seqs = input_ids.tolist()
        device = input_ids.device
        mask_positions, use_gmasks = [], []
        for seq in seqs:
            mask_token = gMASK if gMASK in seq else MASK
            use_gmask = mask_token == gMASK
            mask_positions.append(seq.index(mask_token))
            use_gmasks.append(use_gmask)
        batch_size, seq_length = input_ids.shape
        if use_gmasks is None:
            use_gmasks = [False] * batch_size
        context_lengths = [seq.tolist().index(config.bos_token_id) for seq in input_ids]
        if config.position_encoding_2d:
            position_ids = torch.arange(seq_length, dtype=torch.long, device=device).unsqueeze(0).repeat(batch_size, 1)
            for i, context_length in enumerate(context_lengths):
                position_ids[i, context_length:] = mask_positions[i]
            block_position_ids = [torch.cat((
                torch.zeros(context_length, dtype=torch.long, device=device),
                torch.arange(seq_length - context_length, dtype=torch.long, device=device) + 1
            )) for context_length in context_lengths]
            block_position_ids = torch.stack(block_position_ids, dim=0)
            position_ids = torch.stack((position_ids, block_position_ids), dim=1)
        else:
            position_ids = torch.arange(seq_length, dtype=torch.long, device=device).unsqueeze(0).repeat(batch_size, 1)
            for i, context_length in enumerate(context_lengths):
                if not use_gmasks[i]:
                    position_ids[i, context_length:] = mask_positions[i]
        return position_ids

    def prepare_inputs_for_generation(self,
                                      input_ids: Optional[torch.Tensor] = None,
                                      inputs_embeds: Optional[torch.Tensor] = None,
                                      past_key_values: Optional[list] = None,
                                      attention_mask: Optional[torch.Tensor] = None,
                                      **kwargs):
        self._set_use_cache(self.layers, kwargs.get("use_cache", self.generation_config.use_cache))
        if past_key_values is None:
            self._clean_past_key_values(self.layers)
        else:
            if input_ids is not None:
                input_ids = input_ids[:, -1].unsqueeze(-1)
            else:
                inputs_embeds = inputs_embeds[:, -1, :].unsqueeze(-1)
            self._set_past_key_values(self.layers, past_key_values)
        inputs = {}
        if input_ids is not None:
            inputs["input_ids"] = input_ids
        if attention_mask is not None:
            inputs["attention_mask"] = attention_mask
        if inputs_embeds is not None:
            inputs["inputs_embeds"] = inputs_embeds
        return inputs

    def clean(self):
        self._clean_hidden_states([*self.layers, self.lm_head])
        # 别忘了清理 word_embeddings 里的 past_position_ids
        self._clean_past_key_values(self.layers, self.word_embeddings)
        self._set_use_cache(self.layers, False)
        
    @classmethod
    def _get_word_embedding_with_position_ids_cls(cls, config):
        class WordEmbeddingWithPositionIdsAndInputIds(tensor_parallel.VocabParallelEmbedding):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # 这个实际上是 past_position_ids
                self.past_key_values = None
                self.use_cache = True
                
            def forward(self, input_):
                position_ids = cls._get_position_ids(config, input_, None if self.past_key_values is None else self.past_key_values[0])
                if not self.training and self.use_cache:
                    # self.past_key_values = (self.past_key_values, self.past_key_values)
                    self.past_key_values = (position_ids, position_ids)
                return super().forward(input_), input_, position_ids
        return WordEmbeddingWithPositionIdsAndInputIds
    
    @classmethod
    def pipeline_layers(cls, config: CollieConfig):
        """
        Get layers of pipeline.

        :return: list
        """
        if isinstance(config, str):
            config = CollieConfig.from_pretrained(config)
        return [
            TiedLayerSpec(
            "word_embeddings",
            dict_as_params(input_keys="input_ids", output_keys=["hidden_states", "input_ids", "position_ids"]),
            cls._get_word_embedding_with_position_ids_cls(config),
            config.vocab_size,
            config.hidden_size),
            *[LayerSpec(ChatGLMLayer, config, i)
              for i in range(config.num_layers)],
            LayerSpec(dict_as_params(input_keys="hidden_states", output_keys="hidden_states"),
                nn.LayerNorm,
                config.hidden_size,
                eps=config.layernorm_epsilon),
            TiedLayerSpec(
            "word_embeddings",
            dict_as_params(input_keys="hidden_states", output_keys="logits"),
            ColumnParallelLMHead,
            config.hidden_size,
            config.vocab_size,
            bias=False)
        ]

    @staticmethod
    def load_parallel_state_dict(path: str, config: Union[CollieConfig, str],
                                 process_exclusion: bool = False, **kwargs):...
    @staticmethod
    def load_parallel_state_dict(path: str,
                                 config: Union[CollieConfig, str],
                                 process_exclusion: bool = False,
                                 protocol: str = 'file',
                                 format: str = 'hf', **kwargs):
        """
        Load state_dict from ``path``.

        The format of pretrained model should be the same as that of
        `huggingface`.

        :return: state_dict. Note that the state_dict should be processed
            properly to match the current rank.
        """
        assert format in ["hf", "meta"], "Only support hf and meta format"
        if isinstance(config, str):
            config = CollieConfig.from_pretrained(config)
        io_driver = IODriver.from_protocol(protocol)
        if not io_driver.exists(path):
            raise FileNotFoundError(f"folder {path} not found.")
        state_dict = OrderedDict()
        weights = []
        parts = None
        # 如果开启了进程互斥，那么每个进程都会显示进度条，否则只显示 RANK0 的
        hide_progress = not process_exclusion and int(os.environ.get("RANK", "0")) != 0
        if dist.is_initialized() and process_exclusion:
            # 如果启动了进程互斥，则要进行 dist.get_world_size() 次循环
            rank_order = range(dist.get_world_size())
        else:
            # 不开启只进行一次循环
            rank_order = range(1)
        for rank in rank_order:
            # 如果开启了进程互斥，那么只有对应 RANK 的能进入循环；不开启进程互斥的话就都可以进
            if int(os.environ.get("RANK", "0")) == rank or not process_exclusion:
                # PP 分层的方法保存在了 os.environ["COLLIE_PP_PARTS"], 格式类似于 [0, 17, 35], 左闭右开
                if env.is_pipeline:
                    # 保存的是 json 格式
                    parts = env.pipeline_parts
                # 如果存在 pytorch_model.bin.index.json 文件的话，此时不同的 pp 进程可以按需加载自己需要的权重
                if io_driver.exists(os.path.join(path, "pytorch_model.bin.index.json")) and "COLLIE_PP_PARTS" in os.environ.keys():
                    weight_map = json.loads(io_driver.load(os.path.join(path, "pytorch_model.bin.index.json"), mode="r"))["weight_map"]
                    # layers 表示自己需要的层
                    layers = list(range(parts[int(os.environ["COLLIE_PP_RANK"])], parts[int(os.environ["COLLIE_PP_RANK"]) + 1]))
                    # 筛选出形似 model.layers.0 这样的层。包含两个条件：1. 有数字的层；2. 数字加一要在 layers 里面（因为最开始还有个 embedding 占一层）
                    weights.extend([value for key, value in weight_map.items() \
                        if len(key.split(".")) > 2 \
                            and key.split(".")[2].isdigit() \
                                and (int(key.split(".")[2]) + 1) in layers])
                    # 去重
                    weights = list(set(weights))
                    # 继续筛选，如果有 0 层，那么就要加载 embedding；如果有最后一层，那么就要加载 lm_head；如果有倒数第二层，那么就要加载 norm
                    if 0 in layers:
                        weights.append(weight_map["transformer.word_embeddings.weight"])
                    if max(parts) - 1 in layers:
                        weights.append(weight_map["lm_head.weight"])
                    if max(parts) - 2 in layers:
                        weights.append(weight_map["transformer.final_layernorm.weight"])
                        weights.append(weight_map["transformer.final_layernorm.bias"])
                else:
                    # 如果没有 pytorch_model.bin.index.json 文件的话，那么就加载所有的权重
                    weights = [weight for weight in io_driver.list(path) if weight.endswith(".bin")]
                with progress(weights, desc="Loading state dict", total=len(weights), disable=hide_progress) as pbar:
                    for weight in pbar:
                        part_state_dict = io_driver.load(os.path.join(path, weight), mode="rb")
                        for key in list(part_state_dict.keys()):
                            part_state_dict[key.replace("transformer.", "")] = part_state_dict.pop(key)
                        state_dict.update(part_state_dict)
                        del part_state_dict
                if parts is not None:
                    # 这一步是 pp 的复筛
                    layers = list(range(parts[int(os.environ["COLLIE_PP_RANK"])], parts[int(os.environ["COLLIE_PP_RANK"]) + 1]))
                    for key in list(state_dict.keys()):
                        if key.startswith("layers"):
                            layer = int(key.split(".")[1])
                            if layer + 1 in layers:
                                state_dict[key.replace(f"layers.{layer}", f"{layer + 1}")] = state_dict.pop(key)
                            else:
                                # 形似 model.layers.0 这样的层，筛选掉数字加一不在 layers 里面得
                                state_dict.pop(key)
                        if key.endswith("word_embeddings.weight"):
                            if 0 in layers:
                                state_dict["tied_modules.word_embeddings.weight"] = state_dict.pop(key)
                            else:
                                state_dict.pop(key)
                        if key == "final_layernorm.weight":
                            if max(parts) - 2 in layers:
                                state_dict[f"{max(parts) - 2}.weight"] = state_dict.pop(key)
                            else:
                                state_dict.pop(key)
                        if key == "final_layernorm.bias":
                            if max(parts) - 2 in layers:
                                state_dict[f"{max(parts) - 2}.bias"] = state_dict.pop(key)
                            else:
                                state_dict.pop(key)
                        if key.endswith("lm_head.weight"):
                            if max(parts) - 1 in layers:
                                state_dict["tied_modules.word_embeddings.weight"] = state_dict.pop(key)
                            else:
                                state_dict.pop(key)
                # 根据用户配置的新的 tp size 进行分割
                for key in list(state_dict.keys()):
                    filte_list = ["query_key_value.weight", "query_key_value.bias", "dense_h_to_4h.weight", "dense_h_to_4h.bias", "word_embeddings.weight", "lm_head.weight"]
                    need_split = any([key.endswith(filte) for filte in filte_list])
                    if env.pp_size > 1:
                        # embedding 层和 lm_head 都需要切
                        need_split = need_split or int(key.split(".")[0]) == max(parts) - 1
                        need_split = need_split or int(key.split(".")[0]) == min(parts)
                    if need_split:
                        tensor = list(torch.chunk(state_dict[key], config.tp_size, dim=0))[int(os.environ.get("COLLIE_TP_RANK", "0"))].detach().clone()
                        del state_dict[key]
                        if process_exclusion:
                            # CPU 内存回收（速度很慢）
                            gc.collect()
                        state_dict[key] = tensor
                    elif key.endswith("dense.weight") \
                        or key.endswith("dense_4h_to_h.weight"):
                            tensor = list(torch.chunk(state_dict[key], config.tp_size, dim=1))[int(os.environ.get("COLLIE_TP_RANK", "0"))].detach().clone()
                            del state_dict[key]
                            if process_exclusion:
                                # CPU 内存回收（速度很慢）
                                gc.collect()
                            state_dict[key] = tensor
            if dist.is_initialized() and process_exclusion:
                # 如果选择了进程互斥，那么本次循环中不需要加载权重的进程需等待
                dist.barrier()
        return state_dict

    @staticmethod
    def save_parallel_state_dict(state_dict: dict, path: str,
                                 config: CollieConfig,
                                 process_exclusion: bool = False, **kwargs):...
    @staticmethod
    def save_parallel_state_dict(state_dict: dict,
                                 path: str,
                                 config: CollieConfig,
                                 process_exclusion: bool = False,
                                 protocol: str = 'file'):
        """
        Save state_dict to ``path``.

        The format of saved state dict should be the same as that of
        `huggingface`.
        """
        io_driver = IODriver.from_protocol(protocol)
        def reshape_wq_wk(w: torch.Tensor):
            return w.view(config.num_attention_heads,
                          config.hidden_size // config.num_attention_heads // 2,
                          2,
                          config.hidden_size).transpose(1, 2).reshape(config.hidden_size,
                                                                    config.hidden_size)
        # gather to tp rank 0
        if env.is_pipeline:
            layers = env.pipeline_layers_idx
            parts = env.pipeline_parts
            for key in list(state_dict.keys()):
                if key == "tied_modules.word_embeddings.word_embeddings.weight":
                    if 0 in layers:
                        state_dict["transformer.word_embeddings.weight"] = state_dict.pop(key)
                    elif max(layers) - 1 in layers:
                        state_dict["lm_head.weight"] = state_dict.pop(key)
                else:
                    layer = int(key.split(".")[0])
                    if layer == max(parts) - 2:
                        state_dict[key.replace(f"{layer}.", "transformer.final_layernorm.")] = state_dict.pop(key)
                    else:
                        state_dict[key.replace(f"{layer}.", f"transformer.layers.{layer - 1}.")] = state_dict.pop(key)
        if dist.is_initialized() and process_exclusion:
            # 如果启动了进程互斥，则要进行 pp_size 次循环
            rank_order = range(config.pp_size)
        else:
            # 不开启只进行一次循环
            rank_order = range(1)
        dst = parallel_state.get_tensor_model_parallel_src_rank()
        with progress(rank_order, desc="Saving model", disable=int(os.environ.get("RANK", "0")) != 0) as pbar:
            for rank in pbar:
                if env.dp_rank == 0 \
                    and (env.pp_rank == rank
                         or not process_exclusion):
                    if config.tp_size > 1:
                        for key in sorted(list(state_dict.keys())):
                            tensor_list = None
                            if env.tp_rank == 0:
                                tensor_list = [torch.zeros_like(state_dict[key]).to(state_dict[key].dtype).cuda() for _ in range(config.tp_size)]
                            dist.gather(state_dict[key].cuda(), dst=dst, gather_list=tensor_list, group=env.tp_group)
                            if env.tp_rank == 0:
                                filte_list = ["query_key_value.weight", "query_key_value.bias", "dense_h_to_4h.weight", "dense_h_to_4h.bias", "word_embeddings.weight", "lm_head.weight"]
                                need_split = any([key.endswith(filte) for filte in filte_list])
                                if env.pp_size > 1:
                                    # embedding 层和 lm_head 都需要切
                                    need_split = need_split or int(key.split(".")[0]) == max(parts) - 1
                                    need_split = need_split or int(key.split(".")[0]) == min(parts)
                                if need_split:
                                    state_dict[key] = concat_tensor(tensor_list, dim=0)
                                    if process_exclusion:
                                        # CPU 内存回收（速度很慢）
                                        gc.collect()
                                elif key.endswith("dense.weight") \
                                    or key.endswith("dense_4h_to_4.weight.weight"):
                                        state_dict[key] = concat_tensor(tensor_list, dim=1)
                                        if process_exclusion:
                                            # CPU 内存回收（速度很慢）
                                            gc.collect()
                    if env.tp_rank == 0:
                        # Save gathered weights
                        if env.is_pipeline:
                            ckpt_name = f"pytorch_model-{env.pp_rank+1:05d}-of-{config.pp_size:05d}.bin"
                            total_size = 0
                            weight_map = {}
                            for name, weight in state_dict.items():
                                weight_size = weight.numel() * dtype_byte_size(weight.dtype)
                                weight_map[name] = ckpt_name
                                total_size += weight_size
                            index_dict = dict(total_size=total_size, weight_map=weight_map)
                            tmp_index_file = os.path.join(path, "_tmp_index_{}.json")
                            io_driver.save(
                                json.dumps(index_dict), tmp_index_file.format(env.pp_rank)
                            )
                        else:
                            ckpt_name = f"pytorch_model.bin"
                        ckpt_path = os.path.join(path, ckpt_name)
                        io_driver.save(state_dict, ckpt_path)
                if dist.is_initialized() and process_exclusion:
                    dist.barrier()
        if env.rank == 0:
            config.save_pretrained(path)
        if env.rank == 0 and env.is_pipeline:
            # merge
            tmp_index_files = [tmp_index_file.format(i) for i in range(config.pp_size)]
            total_size = 0
            weight_map = {}
            for _file in tmp_index_files:
                _index_dict = json.loads(io_driver.load(_file, mode="r"))
                total_size += _index_dict["total_size"]
                weight_map.update(_index_dict["weight_map"])
                os.remove(_file)
            merged_dict = {
                "metadata": {"total_size": total_size},
                "weight_map": weight_map
            }
            io_driver.save(
                json.dumps(merged_dict, indent=2, sort_keys=True) + "\n",
                os.path.join(path, "pytorch_model.bin.index.json")
            )
        dist.barrier()