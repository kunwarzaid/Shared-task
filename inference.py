import json
import re
import csv
from pathlib import Path
from collections import Counter, defaultdict
import numpy as np
import torch

import evaluate
from bert_score import score as bert_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# ============================================================
# CONFIG
# ============================================================

TEST_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/test"

MODELS = {
    "Mistral-7B-Instruct": "/workspace/data/KZ_2117574/EACL/mistral_7B_Instruct_split",
    "LLaMA2-13B": "/workspace/data/KZ_2117574/EACL/llama_2_13b_split",
    "Qwen-2.5-7B": "/workspace/data/KZ_2117574/EACL/Qwen_2.5_7B_Instruct_split",
}

LANGS = ["English", "Hindi", "Marathi", "Bangla"]

OUTPUT_DIR = "/workspace/data/KZ_2117574/EACL/eval_results"
OUTPUT_DIR.mkdir(exist_ok=True)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

BERT_MODEL = "xlm-roberta-large"
NLI_MODEL = "joeddav/xlm-roberta-large-xnli"
LABEL_ENTAILMENT = 2

N_BOOTSTRAP = 1000
CI_ALPHA = 0.05


# ============================================================
# LOAD METRICS / MODELS
# ============================================================

rouge = evaluate.load("rouge")

nli_tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL)
nli_model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL).to(DEVICE)
nli_model.eval()


# ============================================================
# UTILS
# ============================================================

def safe_read_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def token_f1(pred, gold):
    p, g = tokenize(pred), tokenize(gold)
    if not p or not g:
        return 0.0
    pc, gc = Counter(p), Counter(g)
    overlap = sum((pc & gc).values())
    prec = overlap / len(p)
    rec = overlap / len(g)
    return 0.0 if prec + rec == 0 else 2 * prec * rec / (prec + rec)


def nli_faithfulness(source, summary):
    inputs = nli_tokenizer(
        source,
        summary,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt"
    ).to(DEVICE)

    with torch.no_grad():
        probs = torch.softmax(nli_model(**inputs).logits, dim=-1)

    return probs[:, LABEL_ENTAILMENT].item()


def bootstrap_ci(scores):
    scores = np.array(scores)
    means = []
    n = len(scores)

    for _ in range(N_BOOTSTRAP):
        sample = np.random.choice(scores, n, replace=True)
        means.append(sample.mean())

    low = np.percentile(means, 100 * CI_ALPHA / 2)
    high = np.percentile(means, 100 * (1 - CI_ALPHA / 2))
    return low, high


# ============================================================
# DATA LOADING
# ============================================================

def load_data(test_root, pred_root, lang):
    sources, preds, golds = [], [], []

    dlg_dir = Path(test_root) / lang / "Dialogues"
    gold_dir = Path(test_root) / lang / "Summary_Text"
    pred_dir = Path(pred_root) / lang / "Summary_Text"

    if not dlg_dir.exists():
        return sources, preds, golds

    for dlg_file in dlg_dir.glob("*.jsonl"):
        name = dlg_file.stem + "_summary.txt"

        gold_file = gold_dir / name
        pred_file = pred_dir / name

        if not (gold_file.exists() and pred_file.exists()):
            continue

        rows = safe_read_jsonl(dlg_file)
        source = " ".join(r.get("dialogue", "") for r in rows if isinstance(r, dict))

        gold = gold_file.read_text(encoding="utf-8", errors="replace").strip()
        pred = pred_file.read_text(encoding="utf-8", errors="replace").strip()

        if source and gold and pred:
            sources.append(source)
            golds.append(gold)
            preds.append(pred)

    return sources, preds, golds


# ============================================================
# EVALUATION
# ============================================================

def evaluate_language(lang, pred_root):
    sources, preds, golds = load_data(TEST_DIR, pred_root, lang)
    if len(preds) == 0:
        return None

    rouge_l = rouge.compute(
        predictions=preds,
        references=golds,
        rouge_types=["rougeL"]
    )["rougeL"]

    _, _, bert_f1 = bert_score(
        preds,
        golds,
        model_type=BERT_MODEL,
        device=DEVICE,
        lang="xx"
    )

    token_scores = [token_f1(p, g) for p, g in zip(preds, golds)]
    faith_scores = [nli_faithfulness(s, p) for s, p in zip(sources, preds)]

    return {
        "ROUGE-L": (rouge_l, *bootstrap_ci(token_scores)),
        "BERTScore": (bert_f1.mean().item(), *bootstrap_ci(bert_f1.cpu().numpy())),
        "Token-F1": (np.mean(token_scores), *bootstrap_ci(token_scores)),
        "Faithfulness": (np.mean(faith_scores), *bootstrap_ci(faith_scores)),
        "N": len(preds)
    }


# ============================================================
# MAIN
# ============================================================

def main():
    results = defaultdict(dict)

    for model, path in MODELS.items():
        for lang in LANGS:
            scores = evaluate_language(lang, path)
            if scores:
                results[model][lang] = scores

    # Save JSON
    with open(OUTPUT_DIR / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Save CSV
    with open(OUTPUT_DIR / "results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Model", "Language", "Metric", "Mean", "CI_low", "CI_high", "N"])

        for model in results:
            for lang in results[model]:
                for metric, vals in results[model][lang].items():
                    if metric != "N":
                        writer.writerow([model, lang, metric, *vals, results[model][lang]["N"]])

    print(f"\nSaved results to {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()


error

Successfully installed anyio-4.12.0 bert-score-0.3.13 datasets-4.4.1 dill-0.4.0 evaluate-0.4.6 h11-0.16.0 hf-xet-1.2.1 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-0.36.0 multiprocess-0.70.18 nltk-3.9.2 numpy-1.26.4 nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.19.3 nvidia-nvjitlink-cu12-12.9.86 nvidia-nvtx-cu12-12.1.105 pyarrow-22.0.0 requests-2.32.5 rouge-score-0.1.2 safetensors-0.7.0 sentencepiece-0.2.1 soxr-1.0.0 tokenizers-0.19.1 torch-2.2.2 tqdm-4.67.1 transformers-4.40.2 triton-2.2.0 typing-extensions-4.15.0 xxhash-3.6.0

�WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

y
[notice] A new release of pip is available: 23.2.1 -> 25.3
[notice] To update, run: python -m pip install --upgrade pip

`Traceback (most recent call last):
  File "/workspace/multi_summ/eval.py", line 29, in <module>

Z    OUTPUT_DIR.mkdir(exist_ok=True)
AttributeError: 'str' object has no attribute 'mkdir'
