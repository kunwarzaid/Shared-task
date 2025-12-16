import json
import re
import csv
from pathlib import Path
from collections import Counter
import numpy as np
import torch

import evaluate
from bert_score import score as bert_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# ============================================================
# CONFIG
# ============================================================

TEST_DIR = Path("/workspace/data/test")
PRED_ROOT = Path("/workspace/data/predictions")
OUTPUT_DIR = Path("./eval_results")

LANGS = ["English", "Hindi", "Marathi", "Bangla"]

MODELS = {
    "Mistral-7B-Instruct": "mistral_7B",
    "LLaMA2-13B": "llama2_13B",
    "Gemma-7B": "gemma_7B"
}

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

BERT_MODEL = "xlm-roberta-large"
NLI_MODEL = "joeddav/xlm-roberta-large-xnli"
ENTAILMENT_LABEL = 2


# ============================================================
# LOAD METRICS / MODELS
# ============================================================

rouge = evaluate.load("rouge")

nli_tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL)
nli_model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL).to(DEVICE)
nli_model.eval()

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# UTILS
# ============================================================

def safe_read_jsonl(path):
    rows = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def simple_tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def token_f1(pred, gold):
    p, g = simple_tokenize(pred), simple_tokenize(gold)
    if not p or not g:
        return 0.0

    pc, gc = Counter(p), Counter(g)
    overlap = sum((pc & gc).values())

    precision = overlap / len(p)
    recall = overlap / len(g)

    return 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)


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

    return probs[:, ENTAILMENT_LABEL].item()


# ============================================================
# DATA LOADING
# ============================================================

def load_data(lang, pred_dir):
    sources, preds, golds = [], [], []

    dlg_dir = TEST_DIR / lang / "Dialogues"
    gold_dir = TEST_DIR / lang / "Summary_Text"
    pred_dir = pred_dir / lang / "Summary_Text"

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
            preds.append(pred)
            golds.append(gold)

    return sources, preds, golds


# ============================================================
# EVALUATION
# ============================================================

def evaluate_language(lang, pred_dir):
    sources, preds, golds = load_data(lang, pred_dir)

    if len(preds) == 0:
        return None

    rouge_l = rouge.compute(
        predictions=preds,
        references=golds,
        rouge_types=["rougeL"]
    )["rougeL"]

    _, _, bert_f1 = bert_score(
        preds, golds,
        model_type=BERT_MODEL,
        lang="xx",
        device=DEVICE
    )
    bert_f1 = bert_f1.mean().item()

    token = np.mean([token_f1(p, g) for p, g in zip(preds, golds)])
    faith = np.mean([nli_faithfulness(s, p) for s, p in zip(sources, preds)])

    return {
        "ROUGE-L": rouge_l,
        "BERTScore": bert_f1,
        "Token-F1": token,
        "Faithfulness": faith,
        "N": len(preds)
    }


# ============================================================
# MAIN
# ============================================================

def main():
    results = {}

    for model_name, model_dir in MODELS.items():
        print(f"\nEvaluating {model_name}")
        results[model_name] = {}

        pred_dir = PRED_ROOT / model_dir

        for lang in LANGS:
            scores = evaluate_language(lang, pred_dir)
            if scores:
                results[model_name][lang] = scores
                print(f"  {lang}: done ({scores['N']} samples)")

    save_csv(results)


def save_csv(results):
    out_file = OUTPUT_DIR / "per_language_results.csv"

    header = [
        "Model", "Language",
        "ROUGE-L", "BERTScore",
        "Token-F1", "Faithfulness", "N"
    ]

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for model, langs in results.items():
            for lang, scores in langs.items():
                writer.writerow([
                    model, lang,
                    f"{scores['ROUGE-L']:.4f}",
                    f"{scores['BERTScore']:.4f}",
                    f"{scores['Token-F1']:.4f}",
                    f"{scores['Faithfulness']:.4f}",
                    scores["N"]
                ])

    print(f"\nSaved results to {out_file.resolve()}")


if __name__ == "__main__":
    main()
