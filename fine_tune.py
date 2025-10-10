import os
import json
import zipfile
from pathlib import Path
from typing import List, Dict

import torch
#import evaluate
from datasets import Dataset
from transformers import  AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorWithPadding
from peft import LoraConfig, get_peft_model
from transformers import BitsAndBytesConfig

ZIP_PATH = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Traindev_s.zip"
DATA_DIR = "/workspace/data/KZ_2117574/SharedTask_NLPAI4Health_Train&dev_set"
#TRAIN_ROOT = os.path.join(EXTRACT_DIR, "train")
#DEV_ROOT = os.path.join(EXTRACT_DIR, "dev")
OUTPUT_DIR = "/workspace/data/KZ_2117574/gemma1b_qlora_multilingual_finetune"
BASE_MODEL =  "/workspace/data/KZ_2117574/gemma_3_1b"


#if not os.path.exists(DATA_DIR):
 #   with zipfile.ZipFile(ZIP_PATH, "r") as zf:
  #      zf.extractall("/workspace/data/KZ_2117574")
   # print("Data unzipped!")


def read_jsonl(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                lines.append(json.loads(line))
            except: pass
    return lines

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
                if not fn.endswith(".jsonl"): continue
                dlg_path = os.path.join(dlg_dir, fn)
                text = "\n".join([x.get("dialogue","") for x in read_jsonl(dlg_path)])
                sum_path = os.path.join(sum_dir, fn.replace(".jsonl","_summary.txt"))
                if os.path.exists(sum_path):
                    with open(sum_path,"r",encoding="utf-8") as f: summary=f.read().strip()
                    prompt = f"Summarize the following doctor–patient dialogue in English:\n{text}\nSummary:"
                    examples.append({"text": prompt, "labels": summary})

        # --- QnA ---
        if os.path.isdir(qna_dir):
            for fn in os.listdir(qna_dir):
                if not fn.endswith(".json"): continue
                with open(os.path.join(qna_dir, fn),"r",encoding="utf-8") as f: data=json.load(f)
                qs = data.get("questions",[])
                for qa in qs:
                    q,a = qa.get("question",""), qa.get("answer","")
                    if not q or not a: continue
                    prompt = f"Answer the following question in the same language as the dialogue:\nQuestion: {q}\nAnswer:"
                    examples.append({"text": prompt, "labels": a})
    return examples

train_data = make_examples(os.path.join(DATA_DIR,"train"))
dev_data = make_examples(os.path.join(DATA_DIR,"dev"))
print(f"Loaded {len(train_data)} train and {len(dev_data)} dev examples")


bnb_cfg = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_use_double_quant=True,
                             bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
if tokenizer.pad_token is None: tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(BASE_MODEL,
                                             device_map="auto",
                                             quantization_config=bnb_cfg)

# ---------- APPLY QLORA ----------
lora_cfg = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj","v_proj"],
                      lora_dropout=0.05, task_type="CAUSAL_LM")
model = get_peft_model(model, lora_cfg)
model.print_trainable_parameters()

def tokenize_fn(examples):
    out = tokenizer(examples["text"], truncation=True, max_length=1024)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["labels"], truncation=True, max_length=1024)
    out["labels"] = labels["input_ids"]
    return out

train_ds = Dataset.from_list(train_data).map(tokenize_fn, batched=True)
dev_ds   = Dataset.from_list(dev_data).map(tokenize_fn, batched=True)

# ----------TRAIN ----------
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

print("Starting fine-tuning...")
trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print("Training complete! Model saved to:", OUTPUT_DIR)
