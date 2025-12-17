import os
import re

INPUT_DIR = "input_files"     # folder with 100 .txt files
OUTPUT_DIR = "cleaned_files"  # cleaned output (same filenames)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_text(text: str) -> str:
    # Remove markdown code blocks (if any)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Remove section headers like PATIENT_OVERVIEW:
    text = re.sub(r"\b[A-Z_]{3,}:\s*", "", text)

    # Remove common markdown characters
    text = re.sub(r"[#*_>`]", "", text)

    # Normalize whitespace
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()

def process_files():
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(".txt"):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(f"Processed: {filename}")

if __name__ == "__main__":
    process_files()
