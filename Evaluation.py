import os, json, time, re, random
from pathlib import Path
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from langdetect import detect, DetectorFactory

from huggingface_hub import login

import torch, bitsandbytes as bnb, transformers
print(torch.__version__)
print(torch.version.cuda)      # None = CPU build; must match your system CUDA
print(bnb.__version__)
print(transformers.__version__)

def huggingface_login():
    """
    Logs into the Hugging Face Hub using the user's token.
    """
    # print("Please enter your Hugging Face token. You can generate one at: https://huggingface.co/settings/tokens")
    token = ''
    try:
        # Log in to the Hugging Face Hub
        login(token=token)
        print("Successfully logged into Hugging Face!")
    except Exception as e:
        print(f"Failed to log in: {e}")

huggingface_login()


# Deterministic language detection
DetectorFactory.seed = 42
torch.set_grad_enabled(False)

# ============================================================
# CONFIG
# ============================================================

# Chat model
BASE_MODEL = "meta-llama/Llama-2-13b-chat-hf"

# Root directory containing language subfolders for TEST (inference target)
TEST_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/test"

# Path to the train_split used for few-shot examples
TRAIN_SPLIT_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/train_split"

# Output root directory
OUTPUT_DIR = "/workspace/data/KZ_2117574/EACL/llama_2_13b_split/few_shot"

# Use 4-bit quantization (recommended for 32GB GPU)
USE_4BIT = True

# Only these language folders will be processed (must match folder names)
TARGET_LANGS = ["English", "Hindi", "Bangla"]

# number of few-shot examples per target language (k-shot)
FEW_SHOT_K = 2

# seed for deterministic sampling of few-shot examples
FEW_SHOT_SEED = 42

# Generation length (summary length), not context length
MAX_NEW_TOKENS_SUMMARY = 512


# System message for the chat model
SYSTEM_SUMMARY = (
    "You are a clinical summarization assistant. "
    "Read a doctor–patient dialogue and write a fluent English summary "
    "focusing on diagnosis, symptoms, investigations, management plan, "
    "supportive care, and follow-up. Do not hallucinate new diagnoses or tests. "
    "End your summary with the token <<END>>."
)

# ============================================================
# UTILS
# ============================================================

def tprint(msg: str):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

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
                # Skip malformed lines quietly
                continue
    return rows

def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def detect_lang(text: str) -> str:
    try:
        return detect(text)
    except Exception:
        return "unknown"

def clip_tokens(tokenizer, text: str, max_tokens: int) -> str:
    """
    Clip text to the last `max_tokens` tokens to stay within context.
    """
    ids = tokenizer.encode(text, add_special_tokens=False)
    if len(ids) <= max_tokens:
        return text
    ids = ids[-max_tokens:]
    return tokenizer.decode(ids, skip_special_tokens=True)

def build_messages(system_prompt: str, user_prompt: str):
    """
    Build chat-style messages for Llama-2-13b-chat-hf.
    """
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

def chat_generate(model, tokenizer, messages, max_new_tokens: int) -> str:
    """
    Use the model's chat template to generate a response.
    """
    # Convert messages to a single prompt string using the tokenizer's chat template
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,         # deterministic (you can turn on sampling if desired)
            num_beams=1,
            pad_token_id=tokenizer.eos_token_id
        )

    # We only care about the generated continuation
    gen_ids = output[0][len(inputs.input_ids[0]):]
    return tokenizer.decode(gen_ids, skip_special_tokens=True).strip()

# Few-shot helper
def collect_few_shot_examples(train_split_root: str, lang: str, k: int, seed: int = 42):
    """
    Find up to k (dialogue_text, summary_text) pairs for `lang` from train_split.
    Deterministic shuffle using `seed`.
    Returns list of tuples: [(dialogue_str, summary_str), ...]
    """
    lang_dir = Path(train_split_root) / lang
    dlg_dir = lang_dir / "Dialogues"
    summ_dir = lang_dir / "Summary_Text"
    examples = []

    if not dlg_dir.exists() or not summ_dir.exists():
        return examples

    json_files = sorted(dlg_dir.glob("*.jsonl"))[:100]
    rng = random.Random(seed)

    # collect pairs where both files exist and non-empty
    pairs = []
    for f in json_files:
        summ_file = summ_dir / f"{f.stem}_summary.txt"
        if not summ_file.exists():
            continue
        try:
            # read dialogue
            rows = safe_read_jsonl(f)
            dialogue = " ".join(
                r.get("dialogue", "") if isinstance(r, dict) else str(r)
                for r in rows
            ).strip()
            if not dialogue:
                continue
            # read summary (strip ending tokens if any)
            summary = summ_file.read_text(encoding="utf-8", errors="replace").strip()
            if not summary:
                continue
            pairs.append((f, dialogue, summary))
        except Exception:
            continue

    if not pairs:
        return examples

    rng.shuffle(pairs)
    for (_, dialogue, summary) in pairs[:k]:
        examples.append((dialogue, summary))
    return examples


# ============================================================
# MODEL LOADING
# ============================================================

def load_model(model_id: str, use_4bit: bool = True):
    tprint(f"Loading tokenizer: {model_id}")
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    quant_cfg = None
    if use_4bit:
        quant_cfg = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16
        )

    tprint(f"Loading model from Hugging Face: {model_id}")
    hf_token = os.getenv("HF_TOKEN", None)

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        quantization_config=quant_cfg,
        torch_dtype=torch.float16,
        token=hf_token
    )

    model.eval()
    return model, tokenizer

def get_model_context_length(model) -> int:
    """
    Infer the model's max context length from its config.
    Fallback to 8192 if not explicitly available.
    """
    cfg = model.config
    candidates = [
        getattr(cfg, "max_position_embeddings", None),
        getattr(cfg, "max_sequence_length", None),
        getattr(cfg, "n_positions", None),
        getattr(cfg, "max_context_length", None),
    ]
    for v in candidates:
        if isinstance(v, int) and v > 0:
            return v
    return 8192  # safe default if nothing is defined

# ============================================================
# MAIN PIPELINE – SUMMARY GENERATION WITH CHAT MODEL
# ============================================================

def run_summary_only():
    if not BASE_MODEL:
        raise ValueError("BASE_MODEL is empty. Set a Hugging Face model id.")
    if not TEST_DIR or not OUTPUT_DIR:
        raise ValueError("Please set TEST_DIR and OUTPUT_DIR in the CONFIG section.")

    model, tokenizer = load_model(BASE_MODEL, use_4bit=USE_4BIT)

    # Dynamically set max input tokens from model config
    raw_ctx = get_model_context_length(model)
    # leave room for generated tokens + chat template overhead
    safety_margin = 512 if raw_ctx > 4096 else 256
    max_input_tokens = max(1024, raw_ctx - safety_margin)

    tprint(f"Model reported context length: {raw_ctx} tokens")
    tprint(f"Using {max_input_tokens} tokens for input truncation")

    # Collect language folders to process
    langs = [
        p for p in Path(TEST_DIR).iterdir()
        if p.is_dir() and p.name in TARGET_LANGS
    ]

    tprint(f"Processing languages: {[p.name for p in langs]}")

    for lang_dir in langs:
        lang = lang_dir.name
        dlg_dir = lang_dir / "Dialogues"
        out_lang = Path(OUTPUT_DIR) / lang

        tprint(f"Language: {lang}")

        if not dlg_dir.exists():
            tprint(f"  • No Dialogues directory found for {lang}, skipping.")
            continue

        files = sorted(dlg_dir.glob("*.jsonl"))
        tprint(f"  • Dialogues: {len(files)}")

        for f in tqdm(files, desc=f"{lang} summaries"):
            out_sum_txt = out_lang / "Summary_Text" / f"{f.stem}_summary.txt"

            # Skip if already generated
            if out_sum_txt.exists():
                continue

            rows = safe_read_jsonl(f)
            dialogue = " ".join(
                r.get("dialogue", "") if isinstance(r, dict) else str(r)
                for r in rows
            )

            # Clip dialogue according to model's context length
            dialogue_clip = clip_tokens(tokenizer, dialogue, max_input_tokens)

            # -------------------------
            # Build few-shot prefix (per language) and final user prompt
            # -------------------------
            few_examples = collect_few_shot_examples(TRAIN_SPLIT_DIR, lang, FEW_SHOT_K, seed=FEW_SHOT_SEED)

            few_shot_str = ""
            if few_examples:
                parts = []
                # Determine a conservative clip budget for each example to keep prompt within context
                # We divide available input tokens among examples and the target dialogue.
                # Example clip budget: (max_input_tokens // (FEW_SHOT_K + 1))
                example_clip_budget = max(128, max_input_tokens // (FEW_SHOT_K + 1))
                for i, (ex_dialogue, ex_summary) in enumerate(few_examples, start=1):
                    ex_dialogue_clip = clip_tokens(tokenizer, ex_dialogue, example_clip_budget)
                    ex_summary_clean = ex_summary.replace("<<END>>", "").strip()
                    parts.append(
                        f"Example {i}:\nDialogue:\n{ex_dialogue_clip}\n\n"
                        f"English Summary:\n{ex_summary_clean}\n---"
                    )
                few_shot_str = (
                    "Below are some examples of dialogues with their English summaries.\n\n"
                    + "\n\n".join(parts)
                    + "\n\nNow follow the same format for the next dialogue.\n\n"
                )
            else:
                # If not enough few-shot examples, remain zero-shot
                few_shot_str = ""

            # Prompt composed of few-shot prefix + target dialogue
            user_prompt = (
                f"{few_shot_str}"
                f"Dialogue:\n{dialogue_clip}\n\n"
                f"Write a detailed but concise English clinical summary and end with <<END>>."
            )
            messages = build_messages(SYSTEM_SUMMARY, user_prompt)

            summary_raw = chat_generate(model, tokenizer, messages, MAX_NEW_TOKENS_SUMMARY)

            end_pos = summary_raw.find("<<END>>")
            summary = summary_raw[:end_pos].strip() if end_pos != -1 else summary_raw.strip()

            # Ensure English summary – if not, re-ask explicitly (same as before),
            # but include few-shot prefix so model retains context.
            if detect_lang(summary) != "en":
                user_prompt = (
                    f"{few_shot_str}"
                    f"Dialogue:\n{dialogue_clip}\n\n"
                    "Write ONLY an English clinical summary. Do not include explanations or meta-text. End with <<END>>."
                )
                messages = build_messages(SYSTEM_SUMMARY, user_prompt)
                summary_raw = chat_generate(model, tokenizer, messages, MAX_NEW_TOKENS_SUMMARY)
                end_pos = summary_raw.find("<<END>>")
                summary = summary_raw[:end_pos].strip() if end_pos != -1 else summary_raw.strip()

            write_text(out_sum_txt, summary)

        # Free up GPU memory between languages
        torch.cuda.empty_cache()

    tprint(f"Summary-only inference complete! Saved to: {OUTPUT_DIR}")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run_summary_only()
