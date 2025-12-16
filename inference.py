
p    import evaluate
  File "/usr/local/lib/python3.10/dist-packages/evaluate/__init__.py", line 29, in <module>

�    from .evaluation_suite import EvaluationSuite
  File "/usr/local/lib/python3.10/dist-packages/evaluate/evaluation_suite/__init__.py", line 10, in <module>

�    from ..evaluator import evaluator
  File "/usr/local/lib/python3.10/dist-packages/evaluate/evaluator/__init__.py", line 17, in <module>

�    from transformers.pipelines import SUPPORTED_TASKS as SUPPORTED_PIPELINE_TASKS
  File "/usr/local/lib/python3.10/dist-packages/transformers/pipelines/__init__.py", line 64, in <module>

�    from .document_question_answering import DocumentQuestionAnsweringPipeline
  File "/usr/local/lib/python3.10/dist-packages/transformers/pipelines/document_question_answering.py", line 30, in <module>

�    from .question_answering import select_starts_ends
  File "/usr/local/lib/python3.10/dist-packages/transformers/pipelines/question_answering.py", line 9, in <module>

�    from ..data import SquadExample, SquadFeatures, squad_convert_examples_to_features
  File "/usr/local/lib/python3.10/dist-packages/transformers/data/__init__.py", line 15, in <module>

�    from .data_collator import (
  File "/usr/local/lib/python3.10/dist-packages/transformers/data/data_collator.py", line 763, in <module>

�    class DataCollatorForLanguageModeling(DataCollatorMixin):
  File "/usr/local/lib/python3.10/dist-packages/transformers/data/data_collator.py", line 1233, in DataCollatorForLanguageModeling

�    offsets: np.ndarray[np.ndarray[tuple[int, int]]], special_tokens_mask: np.ndarray[np.ndarray[int]]
TypeError: Too few arguments for numpy.ndarray

removing /jobs/283787
