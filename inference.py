import os, json, time, re, random
from pathlib import Path
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
from langdetect import detect, DetectorFactory
from huggingface_hub import login

import torch, bitsandbytes as bnb, transformers
print(torch.__version__)
print(torch.version.cuda)
print(bnb.__version__)
print(transformers.__version__)

# ============================================================
# AUTH (optional)
# ============================================================

def huggingface_login():
    token = os.getenv("HF_TOKEN", "")
    if token:
        login(token=token)

huggingface_login()

DetectorFactory.seed = 42
torch.set_grad_enabled(False)

# ============================================================
# CONFIG
# ============================================================

BASE_MODEL = "Qwen/Qwen2.5-7B-Instruct"

# 🔴 PATH TO YOUR FINETUNED LoRA ADAPTER
ADAPTER_DIR = "/workspace/data/KZ_2117574/EACL/qwen_2.5_7b_finetuned"

TEST_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/test"
TRAIN_SPLIT_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/train_split"
OUTPUT_DIR = "/workspace/data/KZ_2117574/EACL/Qwen_2.5_7B_Instruct_split/fewshot"

USE_4BIT = True
TARGET_LANGS = ["Bangla", "English", "Hindi", "Marathi"]

FEW_SHOT_K = 2
FEW_SHOT_SEED = 42
MAX_NEW_TOKENS_SUMMARY = 512

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

def tprint(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def safe_read_jsonl(path: Path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except:
                continue
    return rows

def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def detect_lang(text: str):
    try:
        return detect(text)
    except:
        return "unknown"

def clip_tokens(tok, text, max_tokens):
    ids = tok.encode(text, add_special_tokens=False)
    if len(ids) <= max_tokens:
        return text
    return tok.decode(ids[-max_tokens:], skip_special_tokens=True)

def build_messages(system_prompt, user_prompt):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

def chat_generate(model, tokenizer, messages, max_new_tokens):
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer([text], return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            num_beams=1,
            pad_token_id=tokenizer.eos_token_id
        )
    gen = out[0][len(inputs.input_ids[0]):]
    return tokenizer.decode(gen, skip_special_tokens=True).strip()

# ============================================================
# FEW-SHOT SAMPLING
# ============================================================

def collect_few_shot_examples(root, lang, k, seed=42):
    dlg = Path(root) / lang / "Dialogues"
    summ = Path(root) / lang / "Summary_Text"
    if not dlg.exists():
        return []

    files = sorted(dlg.glob("*.jsonl"))[:100]
    random.Random(seed).shuffle(files)

    examples = []
    for f in files:
        sf = summ / f"{f.stem}_summary.txt"
        if not sf.exists():
            continue
        dialogue = " ".join(
            r.get("dialogue", "") for r in safe_read_jsonl(f) if isinstance(r, dict)
        )
        summary = sf.read_text(encoding="utf-8").strip()
        if dialogue and summary:
            examples.append((dialogue, summary))
        if len(examples) == k:
            break
    return examples

# ============================================================
# MODEL LOADING (FINETUNED)
# ============================================================

def load_model(base_model, adapter_dir, use_4bit=True):
    tprint("Loading tokenizer")
    tok = AutoTokenizer.from_pretrained(base_model, use_fast=True)
    tok.pad_token = tok.eos_token

    quant_cfg = BitsAndBytesConfig(
        load_in_4bit=use_4bit,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

    tprint("Loading base model")
    base = AutoModelForCausalLM.from_pretrained(
        base_model,
        device_map="auto",
        quantization_config=quant_cfg,
        torch_dtype=torch.float16,
        trust_remote_code=True
    )

    tprint("Loading fine-tuned LoRA adapter")
    model = PeftModel.from_pretrained(base, adapter_dir)
    model.eval()

    return model, tok

def get_model_context_length(model):
    return getattr(model.config, "max_position_embeddings", 8192)

# ============================================================
# MAIN
# ============================================================

def run_summary_only():
    model, tokenizer = load_model(BASE_MODEL, ADAPTER_DIR, USE_4BIT)

    max_ctx = get_model_context_length(model)
    max_input_tokens = max(1024, max_ctx - 512)

    for lang_dir in Path(TEST_DIR).iterdir():
        if lang_dir.name not in TARGET_LANGS:
            continue

        out_dir = Path(OUTPUT_DIR) / lang_dir.name / "Summary_Text"
        files = sorted((lang_dir / "Dialogues").glob("*.jsonl"))[:100]

        for f in tqdm(files, desc=lang_dir.name):
            out_file = out_dir / f"{f.stem}_summary.txt"
            if out_file.exists():
                continue

            dialogue = " ".join(
                r.get("dialogue", "") for r in safe_read_jsonl(f) if isinstance(r, dict)
            )
            dialogue = clip_tokens(tokenizer, dialogue, max_input_tokens)

            few = collect_few_shot_examples(TRAIN_SPLIT_DIR, lang_dir.name, FEW_SHOT_K)

            prefix = ""
            for i, (d, s) in enumerate(few, 1):
                prefix += f"Example {i}:\nDialogue:\n{clip_tokens(tokenizer,d,512)}\n\nSummary:\n{s}\n---\n"

            user_prompt = (
                f"{prefix}\nDialogue:\n{dialogue}\n\n"
                "Write a detailed English clinical summary and end with <<END>>."
            )

            summary = chat_generate(
                model, tokenizer,
                build_messages(SYSTEM_SUMMARY, user_prompt),
                MAX_NEW_TOKENS_SUMMARY
            )

            summary = summary.split("<<END>>")[0].strip()
            write_text(out_file, summary)

        torch.cuda.empty_cache()

    tprint("Inference complete.")

if __name__ == "__main__":
    run_summary_only()
