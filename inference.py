import os
import re

INPUT_ROOT = "data"          # root folder containing 4 folders
OUTPUT_ROOT = "cleaned_data" # output root

def clean_text(text: str) -> str:
    # Remove markdown code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Remove section headers like PATIENT_OVERVIEW:
    text = re.sub(r"\b[A-Z_]{3,}:\s*", "", text)

    # Remove markdown characters
    text = re.sub(r"[#*_>`]", "", text)

    # Normalize whitespace
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()

def process_folders():
    for root, _, files in os.walk(INPUT_ROOT):
        relative_path = os.path.relpath(root, INPUT_ROOT)
        output_dir = os.path.join(OUTPUT_ROOT, relative_path)

        os.makedirs(output_dir, exist_ok=True)

        for filename in files:
            if not filename.lower().endswith(".txt"):
                continue

            input_path = os.path.join(root, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, "r", encoding="utf-8") as f:
                raw_text = f.read()

            cleaned_text = clean_text(raw_text)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"Processed: {output_path}")

if __name__ == "__main__":
    process_folders()
