import json
import re
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
    "Mistral-7B": "/workspace/data/.../mistral_7B",
    "LLaMA2-13B": "/workspace/data/.../llama2_13B",
    "Gemma-7B": "/workspace/data/.../gemma_7B"
}

LANGS = ["English", "Hindi", "Marathi", "Bangla"]
LANG_SHORT = {"English": "En", "Hindi": "Hi", "Marathi": "Mr", "Bangla": "Bn"}

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

BERT_MODEL = "xlm-roberta-large"
NLI_MODEL = "joeddav/xlm-roberta-large-xnli"


# ============================================================
# LOAD MODELS
# ============================================================

rouge = evaluate.load("rouge")

nli_tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL)
nli_model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL).to(DEVICE)
nli_model.eval()

ENTAILMENT_LABEL = 2


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
    p, g = tokenize(pred), tokenize(g)
    if not p or not g:
        return 0.0
    pc, gc = Counter(p), Counter(g)
    overlap = sum((pc & gc).values())
    prec = overlap / len(p)
    rec = overlap / len(g)
    return 0.0 if prec + rec == 0 else 2 * prec * rec / (prec + rec)


def faithfulness_nli(source, summary):
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

    return probs[:, ENTAILMENT_LABEL].item()


def load_data(lang, pred_root):
    srcs, preds, golds = [], [], []

    dlg_dir = Path(TEST_DIR) / lang / "Dialogues"
    gold_dir = Path(TEST_DIR) / lang / "Summary_Text"
    pred_dir = Path(pred_root) / lang / "Summary_Text"

    for dlg_file in dlg_dir.glob("*.jsonl"):
        name = dlg_file.stem + "_summary.txt"
        gold_file = gold_dir / name
        pred_file = pred_dir / name

        if not gold_file.exists() or not pred_file.exists():
            continue

        rows = safe_read_jsonl(dlg_file)
        source = " ".join(r.get("dialogue", "") for r in rows if isinstance(r, dict))
        gold = gold_file.read_text(encoding="utf-8", errors="replace").strip()
        pred = pred_file.read_text(encoding="utf-8", errors="replace").strip()

        if source and gold and pred:
            srcs.append(source)
            golds.append(gold)
            preds.append(pred)

    return srcs, preds, golds


# ============================================================
# EVALUATION
# ============================================================

def evaluate_model(model_name, pred_root):
    results = defaultdict(dict)

    for lang in LANGS:
        srcs, preds, golds = load_data(lang, pred_root)
        if not preds:
            continue

        rouge_l = rouge.compute(
            predictions=preds,
            references=golds,
            rouge_types=["rougeL"]
        )["rougeL"]

        _, _, bert_f1 = bert_score(
            preds,
            golds,
            model_type=BERT_MODEL,
            lang="xx",
            device=DEVICE
        )
        bert_f1 = bert_f1.mean().item()

        token = np.mean([token_f1(p, g) for p, g in zip(preds, golds)])
        faith = np.mean([faithfulness_nli(s, p) for s, p in zip(srcs, preds)])

        results[lang] = {
            "ROUGE-L": rouge_l,
            "BERTScore": bert_f1,
            "Token-F1": token,
            "Faithfulness": faith
        }

    return results


# ============================================================
# LATEX TABLE PRINTER
# ============================================================

def print_latex_table(all_results, metric):
    print(f"\n% {metric}")
    print("\\begin{tabular}{lccccc}")
    print("\\toprule")
    print("Model & En & Hi & Mr & Bn & Macro \\\\")
    print("\\midrule")

    best = defaultdict(float)
    for lang in LANGS:
        best[lang] = max(
            all_results[m][lang][metric]
            for m in all_results
            if lang in all_results[m]
        )

    best["Macro"] = 0

    for model, scores in all_results.items():
        row = [model]
        vals = []

        for lang in LANGS:
            v = scores[lang][metric]
            vals.append(v)
            if v == best[lang]:
                row.append(f"\\textbf{{{v:.3f}}}")
            else:
                row.append(f"{v:.3f}")

        macro = np.mean(vals)
        row.append(f"{macro:.3f}")

        print(" & ".join(row) + " \\\\")

    print("\\bottomrule")
    print("\\end{tabular}")


# ============================================================
# MAIN
# ============================================================

def main():
    all_results = {}

    for model_name, pred_root in MODELS.items():
        print(f"Evaluating {model_name}")
        all_results[model_name] = evaluate_model(model_name, pred_root)

    for metric in ["ROUGE-L", "BERTScore", "Token-F1", "Faithfulness"]:
        print_latex_table(all_results, metric)


if __name__ == "__main__":
    main()
