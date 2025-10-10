import os
import json
from pathlib import Path
from typing import List, Dict

import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model
from transformers import BitsAndBytesConfig


# --- PATHS ---
ZIP_PATH = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Traindev_s.zip"
DATA_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set"
OUTPUT_DIR = "/workspace/data/KZ_2117574/gemma1b_qlora_multilingual_finetune"
BASE_MODEL = "/workspace/data/KZ_2117574/gemma_3_1b"


# --- SAFE JSONL READER ---
def read_jsonl(path):
    """Read JSONL file safely, skip broken lines."""
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                # skip invalid lines
                continue
    return records


def make_examples(root):
    examples = []

    for lang in os.listdir(root):
        lang_path = os.path.join(root, lang)
        if not os.path.isdir(lang_path):
            continue

        dlg_dir = os.path.join(lang_path, "Dialogues")
        sum_dir = os.path.join(lang_path, "Summary_Text")
        qna_dir = os.path.join(lang_path, "QnA")

        # --- Summarization ---
        if os.path.isdir(dlg_dir) and os.path.isdir(sum_dir):
            for fn in os.listdir(dlg_dir):
                if not fn.endswith(".jsonl"):
                    continue

                dlg_path = os.path.join(dlg_dir, fn)
                records = read_jsonl(dlg_path)

                # Flatten any list entries and safely convert all to strings
                dialogue_text = "\n".join([
                    " ".join(x["dialogue"]) if isinstance(x.get("dialogue"), list)
                    else str(x.get("dialogue", "")) if isinstance(x, dict)
                    else str(x)
                    for x in records
                ])

                sum_path = os.path.join(sum_dir, fn.replace(".jsonl", "_summary.txt"))
                if os.path.exists(sum_path):
                    with open(sum_path, "r", encoding="utf-8") as f:
                        summary = f.read().strip()

                    prompt = (
                        f"Summarize the following doctor–patient dialogue in English.\n\n"
                        f"Dialogue:\n{dialogue_text}\n\nSummary:"
                    )

                    examples.append({"text": prompt, "labels": summary})

        # --- QnA ---
        if os.path.isdir(qna_dir):
            for fn in os.listdir(qna_dir):
                if not fn.endswith(".json"):
                    continue

                with open(os.path.join(qna_dir, fn), "r", encoding="utf-8") as f:
                    data = json.load(f)

                qs = data.get("questions", [])
                for qa in qs:
                    q, a = qa.get("question", ""), qa.get("answer", "")
                    if not q or not a:
                        continue

                    prompt = (
                        f"Answer the following question in the same language as the dialogue:\n"
                        f"Question: {q}\nAnswer:"
                    )
                    examples.append({"text": prompt, "labels": a})

    return examples



# --- LOAD DATA ---
train_data = make_examples(os.path.join(DATA_DIR, "train"))
dev_data = make_examples(os.path.join(DATA_DIR, "dev"))
print(f"✅ Loaded {len(train_data)} train and {len(dev_data)} dev examples")


# --- MODEL + QLoRA ---
bnb_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    device_map="auto",
    quantization_config=bnb_cfg
)

# Apply LoRA
lora_cfg = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_cfg)
model.print_trainable_parameters()


# --- TOKENIZATION ---
def tokenize_fn(examples):
    model_inputs = tokenizer(examples["text"], truncation=True, max_length=1024)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["labels"], truncation=True, max_length=1024)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


train_ds = Dataset.from_list(train_data).map(tokenize_fn, batched=True)
dev_ds = Dataset.from_list(dev_data).map(tokenize_fn, batched=True)


# --- TRAINING ---
args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    num_train_epochs=2,
    learning_rate=2e-4,
    fp16=True,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_steps=20,
    report_to="none"
)

collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_ds,
    eval_dataset=dev_ds,
    data_collator=collator
)

print("🚀 Starting fine-tuning...")
trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print("✅ Training complete! Model saved to:", OUTPUT_DIR)
