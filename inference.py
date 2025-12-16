2`torch_dtype` is deprecated! Use `dtype` instead!

Fetching 4 files:   0%|          | 0/4 [00:00<?, ?it/s]
Fetching 4 files:  25%|██▌       | 1/4 [02:34<07:42, 154.04s/it]
Fetching 4 files: 100%|██████████| 4/4 [02:34<00:00, 38.51s/it] 

Loading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]
Loading checkpoint shards:  25%|██▌       | 1/4 [00:03<00:09,  3.15s/it]
Loading checkpoint shards:  50%|█████     | 2/4 [00:07<00:07,  3.61s/it]
Loading checkpoint shards:  75%|███████▌  | 3/4 [00:11<00:03,  3.77s/it]
Loading checkpoint shards: 100%|██████████| 4/4 [00:13<00:00,  3.44s/it]

+[06:55:35] Loading fine-tuned LoRA adapter

/<class 'peft.peft_model.PeftModelForCausalLM'>

Marathi:   0%|          | 0/100 [00:00<?, ?it/s]
�Token indices sequence length is longer than the specified maximum sequence length for this model (191090 > 131072). Running this sequence through the model will result in indexing errors

�The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.

Marathi:   0%|          | 0/100 [00:14<?, ?it/s]

qTraceback (most recent call last):
  File "/workspace/multi_summ/inference_qwen_fine1.py", line 227, in <module>

m    run_summary_only()
  File "/workspace/multi_summ/inference_qwen_fine1.py", line 213, in run_summary_only

p    summary = chat_generate(
  File "/workspace/multi_summ/inference_qwen_fine1.py", line 103, in chat_generate

v    out = model.generate(
  File "/usr/local/lib/python3.10/dist-packages/peft/peft_model.py", line 1190, in generate

�    outputs = self.base_model.generate(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context

�    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 2564, in generate

�    result = decoding_method(
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 2784, in _sample

�    outputs = self(**model_inputs, return_dict=True)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl

�    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl

�    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/hooks.py", line 170, in new_forward

�    output = module._old_forward(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/generic.py", line 918, in wrapper

�    output = func(self, *args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/qwen2/modeling_qwen2.py", line 449, in forward

�    outputs: BaseModelOutputWithPast = self.model(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl

�    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl

�    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/hooks.py", line 170, in new_forward

�    output = module._old_forward(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/generic.py", line 1072, in wrapper

�    outputs = func(self, *args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/qwen2/modeling_qwen2.py", line 384, in forward

�    hidden_states = decoder_layer(
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_layers.py", line 94, in __call__

�    return super().__call__(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl

�    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl

�    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/hooks.py", line 170, in new_forward

�    output = module._old_forward(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/deprecation.py", line 172, in wrapped_func

�    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/qwen2/modeling_qwen2.py", line 249, in forward

�    hidden_states = self.mlp(hidden_states)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl

�    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl

�    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/hooks.py", line 170, in new_forward

�    output = module._old_forward(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/qwen2/modeling_qwen2.py", line 46, in forward

Q    down_proj = self.down_proj(self.act_fn(self.gate_proj(x)) * self.up_proj(x))

 torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 6.74 GiB. GPU 0 has a total capacity of 31.75 GiB of which 4.80 GiB is free. Process 3695566 has 26.94 GiB memory in use. Of the allocated memory 23.26 GiB is allocated by PyTorch, and 3.31 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

removing /jobs/283642
