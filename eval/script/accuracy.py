import json
import re
from typing import Optional, List, Dict


OPTION_PATTERN = re.compile(
    r"\b([A-Z])\b|^([A-Z])[\.\):]|option\s*([A-Z])|answer\s*is\s*([A-Z])",
    re.IGNORECASE
)


def extract_option(text: str) -> Optional[str]:
    """
    Extract MCQ option (A-Z) from a text string.
    
    Handles cases like:
    - "A"
    - "A."
    - "A. some text"
    - "option B"
    - "The answer is C"
    - "c) because ..."
    
    Returns:
        Uppercase option letter (e.g. "A"), or None if not found.
    """
    if not text or not isinstance(text, str):
        return None

    text = text.strip().upper()

    # First try regex patterns
    match = OPTION_PATTERN.search(text)
    if match:
        for group in match.groups():
            if group:
                return group.upper()

    # Fallback: first character heuristic
    if len(text) > 0 and text[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return text[0]

    return None


def load_json_or_jsonl(path: str) -> List[Dict]:
    """
    Load JSON or JSONL file.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if content.startswith("["):
        return json.loads(content)
    else:
        return [json.loads(line) for line in content.splitlines() if line.strip()]


def compute_mcq_accuracy(
    json_path: str,
    gt_key: str = "ground_truth",
    pred_key: str = "response",
    verbose: bool = True,
):
    """
    Compute MCQ accuracy from a JSON / JSONL file.

    Args:
        json_path: path to json or jsonl file
        gt_key: key name for ground truth
        pred_key: key name for model response
        verbose: whether to print detailed stats

    Returns:
        accuracy (float)
    """
    data = load_json_or_jsonl(json_path)

    total = len(data)
    valid = 0
    correct = 0
    invalid = 0

    for idx, item in enumerate(data):
        gt_raw = item.get(gt_key, "")
        pred_raw = item.get(pred_key, "")

        gt_option = extract_option(gt_raw)
        pred_option = extract_option(pred_raw)

        if gt_option is None or pred_option is None:
            invalid += 1
            continue

        valid += 1
        if gt_option == pred_option:
            correct += 1

    acc = correct / valid if valid > 0 else 0.0

    if verbose:
        print("=" * 50)
        print("MCQ Accuracy Evaluation")
        print("=" * 50)
        print(f"Total samples      : {total}")
        print(f"Valid samples      : {valid}")
        print(f"Invalid samples    : {invalid}")
        print(f"Correct predictions: {correct}")
        print(f"Accuracy (ACC)     : {acc:.2f}")
        print("=" * 50)

    return acc


if __name__ == "__main__":
    # Example usage
    json_file = "predictions.json"
    compute_mcq_accuracy(json_file)