def evaluate_language(lang, pred_root):
    sources, preds, golds = load_data(TEST_DIR, pred_root, lang)
    if len(preds) == 0:
        return None

    # -------- ROUGE (per-example) --------
    rouge_scores = rouge.compute(
        predictions=preds,
        references=golds,
        rouge_types=["rougeL"],
        use_aggregator=False
    )["rougeL"]

    rouge_mean = float(np.mean(rouge_scores))
    rouge_ci = bootstrap_ci(rouge_scores)

    # -------- BERTScore (per-example) --------
    _, _, bert_f1 = bert_score(
        preds,
        golds,
        model_type=BERT_MODEL,
        device=DEVICE,
        lang="xx"
    )

    bert_scores = bert_f1.cpu().numpy()
    bert_mean = float(bert_scores.mean())
    bert_ci = bootstrap_ci(bert_scores)

    # -------- Token F1 --------
    token_scores = [token_f1(p, g) for p, g in zip(preds, golds)]
    token_mean = float(np.mean(token_scores))
    token_ci = bootstrap_ci(token_scores)

    # -------- Faithfulness --------
    faith_scores = [nli_faithfulness(s, p) for s, p in zip(sources, preds)]
    faith_mean = float(np.mean(faith_scores))
    faith_ci = bootstrap_ci(faith_scores)

    return {
        "ROUGE-L": (rouge_mean, *rouge_ci),
        "BERTScore": (bert_mean, *bert_ci),
        "Token-F1": (token_mean, *token_ci),
        "Faithfulness": (faith_mean, *faith_ci),
        "N": len(preds)
    }
