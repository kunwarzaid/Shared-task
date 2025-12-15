import os
import json
from pathlib import Path
from collections import Counter
import numpy as np
import torch

import evaluate
from bert_score import score as bert_score
from summac.model_summac import SummaCZS

import nltk
nltk.download("punkt")
from nltk.tokenize import word_tokenize


# ============================================================
# CONFIG
# ============================================================

# Gold summaries + source dialogues (test split)
TEST_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/test"

# Model predictions
PRED_DIR = "/workspace/data/KZ_2117574/EACL/mistral_7B_Instruct_split"

LANGS = ["English", "Hindi", "Marathi", "Bangla"]

# BERTScore backbone (English summaries)
BERT_MODEL = "microsoft/deberta-xlarge-mnli"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# ============================================================
# METRICS INITIALIZATION
# ============================================================

rouge = evaluate.load("rouge")

summac = SummaCZS(
    granularity="sentence",
    model_name="roberta-large-mnli",
    device=DEVICE
)


# ============================================================
# UTILS
# ============================================================

def safe_read_jsonl(path: Path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            try:
                rows.append(json.loads(s))
            except Exception:
                continue
    return rows


def compute_token_f1(pred: str, gold: str):
    pred_tokens = word_tokenize(pred.lower())
    gold_tokens = word_tokenize(gold.lower())

    if not pred_tokens or not gold_tokens:
        return 0.0

    pred_counter = Counter(pred_tokens)
    gold_counter = Counter(gold_tokens)

    overlap = sum((pred_counter & gold_counter).values())

    precision = overlap / len(pred_tokens)
    recall = overlap / len(gold_tokens)

    if precision + recall == 0:
        return 0.0

    return 2 * precision * recall / (precision + recall)


# ============================================================
# LOAD DATA (SOURCE + GOLD + PRED)
# ============================================================

def load_data(test_root: str, pred_root: str, langs):
    sources = []
    golds = []
    preds = []

    for lang in langs:
        dlg_dir = Path(test_root) / lang / "Dialogues"
        gold_dir = Path(test_root) / lang / "Summary_Text"
        pred_dir = Path(pred_root) / lang / "Summary_Text"

        if not (dlg_dir.exists() and gold_dir.exists() and pred_dir.exists()):
            print(f"[WARN] Missing directories for {lang}, skipping.")
            continue

        for dlg_file in sorted(dlg_dir.glob("*.jsonl")):
            summ_name = f"{dlg_file.stem}_summary.txt"

            gold_file = gold_dir / summ_name
            pred_file = pred_dir / summ_name

            if not (gold_file.exists() and pred_file.exists()):
                continue

            rows = safe_read_jsonl(dlg_file)
            source = " ".join(
                r.get("dialogue", "") if isinstance(r, dict) else str(r)
                for r in rows
            ).strip()

            gold = gold_file.read_text(encoding="utf-8", errors="replace").strip()
            pred = pred_file.read_text(encoding="utf-8", errors="replace").strip()

            if source and gold and pred:
                sources.append(source)
                golds.append(gold)
                preds.append(pred)

    return sources, preds, golds


# ============================================================
# MAIN EVALUATION
# ============================================================

def main():
    sources, preds, golds = load_data(TEST_DIR, PRED_DIR, LANGS)

    assert len(preds) == len(golds) == len(sources)
    print(f"Evaluating {len(preds)} examples")

    # --------------------
    # ROUGE-L (F1)
    # --------------------
    rouge_scores = rouge.compute(
        predictions=preds,
        references=golds,
        rouge_types=["rougeL"]
    )
    rouge_l_f1 = rouge_scores["rougeL"]

    # --------------------
    # BERTScore (F1)
    # --------------------
    _, _, bert_f1 = bert_score(
        preds,
        golds,
        model_type=BERT_MODEL,
        lang="en",
        device=DEVICE,
        verbose=True
    )
    bert_f1 = bert_f1.mean().item()

    # --------------------
    # Token-level F1
    # --------------------
    token_f1s = [compute_token_f1(p, g) for p, g in zip(preds, golds)]
    token_f1 = float(np.mean(token_f1s))

    # --------------------
    # SummaC-ZS (faithfulness)
    # --------------------
    summac_scores = []
    for src, pred in zip(sources, preds):
        score = summac.score([src], [pred])["score"]
        summac_scores.append(score)

    summac_score = float(np.mean(summac_scores))

    # --------------------
    # RESULTS
    # --------------------
    print("\n===== FINAL EVALUATION RESULTS =====")
    print(f"ROUGE-L (F1):        {rouge_l_f1:.4f}")
    print(f"BERTScore (F1):     {bert_f1:.4f}")
    print(f"Token-level F1:     {token_f1:.4f}")
    print(f"SummaC-ZS:          {summac_score:.4f}")
    print("===================================")


if __name__ == "__main__":
    main()
