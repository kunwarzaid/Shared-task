Downloading builder script: 0.00B [00:00, ?B/s]
Downloading builder script: 6.14kB [00:00, 14.4MB/s]

�Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/import_utils.py", line 2317, in __getattr__

�    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/import_utils.py", line 2347, in _get_module

{    raise e
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/import_utils.py", line 2345, in _get_module

�    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module

�    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import

E  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load

N  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked

D  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked

J  File "<frozen importlib._bootstrap_external>", line 883, in exec_module

O  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed

  File "/usr/local/lib/python3.10/dist-packages/transformers/models/xlm_roberta/modeling_xlm_roberta.py", line 29, in <module>

�    from ...modeling_layers import GradientCheckpointingLayer
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_layers.py", line 28, in <module>

�    from .processing_utils import Unpack
  File "/usr/local/lib/python3.10/dist-packages/transformers/processing_utils.py", line 34, in <module>

�    from .audio_utils import AudioInput, load_audio
  File "/usr/local/lib/python3.10/dist-packages/transformers/audio_utils.py", line 52, in <module>

�    import soxr
ModuleNotFoundError: No module named 'soxr'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/multi_summ/eval.py", line 48, in <module>

�    nli_model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL).to(DEVICE)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 601, in from_pretrained

�    model_class = _get_model_class(config, cls._model_mapping)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 394, in _get_model_class

�    supported_models = model_mapping[type(config)]
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 807, in __getitem__

�    return self._load_attr_from_module(model_type, model_name)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 821, in _load_attr_from_module

�    return getattribute_from_module(self._modules[module_name], attr)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 733, in getattribute_from_module

�    if hasattr(module, attr):
  File "/usr/local/lib/python3.10/dist-packages/transformers/utils/import_utils.py", line 2320, in __getattr__

�    raise ModuleNotFoundError(
ModuleNotFoundError: Could not import module 'XLMRobertaForSequenceClassification'. Are this object's requirements defined correctly?
