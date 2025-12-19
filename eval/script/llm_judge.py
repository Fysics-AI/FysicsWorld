import os
import json
from typing import List, Dict
from openai import OpenAI


def create_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Please export it before running."
        )
    return OpenAI(api_key=api_key)


EVAL_PROMPT_TEMPLATE = """
## System Instruction
You are an **EXTREMELY STRICT** evaluator for image understanding open-ended QA tasks.  
Your job is to judge whether the **Model Response** is **correct or incorrect** compared to the **Ground Truth**, based solely on the content of the **IMAGE**.
Your evaluation must be:
- **Binary**: "Correct" or "Incorrect" (no partial credit).
- **Objective**: Do not guess, infer, or assume information not visible in the image.
- **Consistent**: Follow the rules exactly.
- **Ruthlessly strict**: Any uncertainty → mark as Incorrect.
## Input Parameters
You will be given:
- **IMAGE**: The image the model was asked to analyze; **QUESTION**: The original question about the image; **GROUND_TRUTH**: The correct answer; **RESPONSE**: The model's predicted answer.
## Evaluation Rules
### 1. Exactness of Meaning
Declare **Correct** only if the RESPONSE expresses the **same meaning** as the GROUND_TRUTH.
- Synonyms are allowed if meaning is perfectly equivalent; Minor wording differences are allowed, *but not* meaning changes.
### 2. Visual Evidence Requirement
The RESPONSE must be fully supported by visible evidence in the IMAGE.
- If the RESPONSE includes extra details not present in the image → **Incorrect**; If the RESPONSE contradicts visual evidence → **Incorrect**.
### 3. No Guessing
If the image does NOT clearly provide enough information to validate the RESPONSE:
- Mark **Incorrect**, even if the guess happens to match GROUND_TRUTH.
### 4. Numerical Strictness
For numbers, counts, attributes:
- Must match exactly unless GROUND_TRUTH explicitly gives a range; If RESPONSE gives a range but GT gives single value → Incorrect; If RESPONSE gives a single value but GT gives a range → Incorrect.
### 5. Attribute Strictness
For color, type, identity, text (OCR), and object category:
- Must match Ground Truth exactly; If RESPONSE is more specific than GT and unverifiable → Incorrect; If RESPONSE is vaguer than GT → Incorrect.
### 6. OCR-Specific
If the QUESTION requires reading text:
- The RESPONSE must match the text exactly (case-insensitive); Any missing character, extra character, or misreading → Incorrect.
### 7. Ambiguity Resolution
If either:
- the GROUND_TRUTH is ambiguous, or the image is ambiguous  
→ You must assume the RESPONSE is **Incorrect** unless it *exactly* matches GT with no contradiction.
## Output Format
**You must output exactly one word**: `CORRECT`  **or** `INCORRECT`
No explanation. No additional text.

QUESTION:
{question}

GROUND_TRUTH:
{ground_truth}

RESPONSE:
{model_answer}
""".strip()


def build_eval_prompt(
    question: str,
    ground_truth: str,
    model_answer: str,
) -> str:
    return EVAL_PROMPT_TEMPLATE.format(
        question=question,
        ground_truth=ground_truth,
        model_answer=model_answer,
    )


def load_json_or_jsonl(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if content.startswith("["):
        return json.loads(content)
    else:
        return [json.loads(line) for line in content.splitlines() if line.strip()]



def evaluate_single_sample(
    client: OpenAI,
    question: str,
    ground_truth: str,
    model_answer: str,
    model_name: str = "gpt-5",
) -> bool:
    prompt = build_eval_prompt(question, ground_truth, model_answer)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a strict and unbiased evaluator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )

    verdict = response.choices[0].message.content.strip().upper()
    return verdict == "CORRECT"


def compute_open_ended_accuracy(
    json_path: str,
    question_key: str = "question",
    gt_key: str = "ground_truth",
    pred_key: str = "response",
    model_name: str = "gpt-5",
    verbose: bool = True,
) -> float:
    data = load_json_or_jsonl(json_path)
    client = create_openai_client()

    total = len(data)
    correct = 0
    invalid = 0

    for idx, item in enumerate(data):
        question = item.get(question_key, "")
        ground_truth = item.get(gt_key, "")
        model_answer = item.get(pred_key, "")

        if not question or not ground_truth or not model_answer:
            invalid += 1
            continue

        try:
            is_correct = evaluate_single_sample(
                client,
                question,
                ground_truth,
                model_answer,
                model_name=model_name,
            )
            if is_correct:
                correct += 1
        except Exception as e:
            invalid += 1
            if verbose:
                print(f"[Error] Sample {idx}: {e}")

    valid = total - invalid
    acc = correct / valid if valid > 0 else 0.0

    if verbose:
        print("=" * 60)
        print("Open-ended QA Accuracy Evaluation")
        print("=" * 60)
        print(f"Total samples   : {total}")
        print(f"Valid samples   : {valid}")
        print(f"Invalid samples : {invalid}")
        print(f"Correct         : {correct}")
        print(f"Accuracy (ACC)  : {acc:.4f}")
        print("=" * 60)

    return acc


if __name__ == "__main__":
    json_file = "predictions.json"
    compute_open_ended_accuracy(json_file)