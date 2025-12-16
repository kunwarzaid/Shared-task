import os, json, time, random
from pathlib import Path
from tqdm import tqdm

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
from langdetect import detect, DetectorFactory

# ============================================================
# ENV + LOGS
# ============================================================

DetectorFactory.seed = 42
torch.set_grad_enabled(False)

print("Torch:", torch.__version__)
print("CUDA:", torch.version.cuda)

# ============================================================
# CONFIG
# ============================================================

BASE_MODEL = "Qwen/Qwen2.5-7B-Instruct"

# 🔴 PATH TO YOUR FINETUNED LoRA ADAPTER DIRECTORY
ADAPTER_DIR = "/workspace/data/KZ_2117574/EACL/qwen_2.5_7b_finetuned"

TEST_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/test"
TRAIN_SPLIT_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set/train_split"
OUTPUT_DIR = "/workspace/data/KZ_2117574/EACL/Qwen_2.5_7B_Instruct_split/fewshot"

TARGET_LANGS = ["Bangla", "English", "Hindi", "Marathi"]

USE_4BIT = True
FEW_SHOT_K = 2
FEW_SHOT_SEED = 42

# 🔒 HARD MEMORY-SAFE LIMITS (CRITICAL)
MAX_TOTAL_INPUT_TOKENS = 8192
TARGET_DIALOGUE_TOKENS = 2048
EXAMPLE_DIALOGUE_TOKENS = 512

MAX_NEW_TOKENS_SUMMARY = 512
MAX_TEST_EXAMPLES = 100

SYSTEM_SUMMARY = (
    "You are a clinical summarization assistant. "
    "Read a doctor–patient dialogue and write a fluent English summary "
    "focusing on diagnosis, symptoms, investigations, management plan, "
    "supportive care, and follow-up. "
    "Do not hallucinate new diagnoses or tests. "
    "End your summary with the token <<END>>."
)

# ============================================================
# UTILS
# ============================================================

def tprint(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def safe_read_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except:
                continue
    return rows

def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def detect_lang(text):
    try:
        return detect(text)
    except:
        return "unknown"

def clip_tokens(tokenizer, text, max_tokens):
    ids = tokenizer.encode(text, add_special_tokens=False)
    if len(ids) <= max_tokens:
        return text
    return tokenizer.decode(ids[-max_tokens:], skip_special_tokens=True)

def clip_prompt_after_template(tokenizer, text, max_tokens):
    ids = tokenizer.encode(text, add_special_tokens=False)
    if len(ids) <= max_tokens:
        return text
    return tokenizer.decode(ids[-max_tokens:], skip_special_tokens=True)

def build_messages(system_prompt, user_prompt):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

# ============================================================
# FEW-SHOT EXAMPLES
# ============================================================

def collect_few_shot_examples(root, lang, k, seed):
    rng = random.Random(seed)
    dlg_dir = Path(root) / lang / "Dialogues"
    sum_dir = Path(root) / lang / "Summary_Text"

    if not dlg_dir.exists():
        return []

    files = sorted(dlg_dir.glob("*.jsonl"))[:100]
    rng.shuffle(files)

    examples = []
    for f in files:
        sfile = sum_dir / f"{f.stem}_summary.txt"
        if not sfile.exists():
            continue

        dialogue = " ".join(
            r.get("dialogue", "")
            for r in safe_read_jsonl(f)
            if isinstance(r, dict)
        ).strip()

        summary = sfile.read_text(encoding="utf-8", errors="replace").strip()
        if dialogue and summary:
            examples.append((dialogue, summary))

        if len(examples) == k:
            break

    return examples

# ============================================================
# MODEL LOADING (FINETUNED)
# ============================================================

def load_model(base_model, adapter_dir):
    tprint("Loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(base_model, use_fast=True)
    tokenizer.pad_token = tokenizer.eos_token

    quant_cfg = BitsAndBytesConfig(
        load_in_4bit=USE_4BIT,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

    tprint("Loading base model")
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model,
        device_map="auto",
        quantization_config=quant_cfg,
        dtype=torch.float16,
        trust_remote_code=True
    )

    tprint("Loading fine-tuned LoRA adapter")
    model = PeftModel.from_pretrained(
        base_model,
        adapter_dir,
        dtype=torch.float16
    )

    model.eval()
    return model, tokenizer

# ============================================================
# GENERATION
# ============================================================

def chat_generate(model, tokenizer, messages):
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # 🔴 HARD CLIP FINAL PROMPT
    prompt = clip_prompt_after_template(
        tokenizer,
        prompt,
        MAX_TOTAL_INPUT_TOKENS
    )

    inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS_SUMMARY,
            do_sample=False,
            num_beams=1,
            use_cache=True,
            pad_token_id=tokenizer.eos_token_id
        )

    gen = output[0][len(inputs.input_ids[0]):]
    return tokenizer.decode(gen, skip_special_tokens=True).strip()

# ============================================================
# MAIN PIPELINE
# ============================================================

def run_summary_only():
    model, tokenizer = load_model(BASE_MODEL, ADAPTER_DIR)

    for lang_dir in Path(TEST_DIR).iterdir():
        if lang_dir.name not in TARGET_LANGS:
            continue

        tprint(f"Language: {lang_dir.name}")
        dlg_dir = lang_dir / "Dialogues"
        out_dir = Path(OUTPUT_DIR) / lang_dir.name / "Summary_Text"

        files = sorted(dlg_dir.glob("*.jsonl"))[:MAX_TEST_EXAMPLES]

        few_shot = collect_few_shot_examples(
            TRAIN_SPLIT_DIR,
            lang_dir.name,
            FEW_SHOT_K,
            FEW_SHOT_SEED
        )

        for f in tqdm(files, desc=lang_dir.name):
            out_file = out_dir / f"{f.stem}_summary.txt"
            if out_file.exists():
                continue

            dialogue = " ".join(
                r.get("dialogue", "")
                for r in safe_read_jsonl(f)
                if isinstance(r, dict)
            )
            dialogue = clip_tokens(tokenizer, dialogue, TARGET_DIALOGUE_TOKENS)

            prefix = ""
            for i, (d, s) in enumerate(few_shot, 1):
                d = clip_tokens(tokenizer, d, EXAMPLE_DIALOGUE_TOKENS)
                s = s.replace("<<END>>", "").strip()
                prefix += (
                    f"Example {i}:\nDialogue:\n{d}\n\n"
                    f"English Summary:\n{s}\n---\n"
                )

            user_prompt = (
                f"{prefix}\nDialogue:\n{dialogue}\n\n"
                "Write a detailed but concise English clinical summary and end with <<END>>."
            )

            summary = chat_generate(
                model,
                tokenizer,
                build_messages(SYSTEM_SUMMARY, user_prompt)
            )

            summary = summary.split("<<END>>")[0].strip()

            # enforce English if needed
            if detect_lang(summary) != "en":
                user_prompt = (
                    f"{prefix}\nDialogue:\n{dialogue}\n\n"
                    "Write ONLY an English clinical summary. End with <<END>>."
                )
                summary = chat_generate(
                    model,
                    tokenizer,
                    build_messages(SYSTEM_SUMMARY, user_prompt)
                )
                summary = summary.split("<<END>>")[0].strip()

            write_text(out_file, summary)

        torch.cuda.empty_cache()

    tprint("Inference complete.")

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run_summary_only()
