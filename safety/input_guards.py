import re
import json
import ollama
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

JUDGE_MODEL = os.getenv("JUDGE_MODEL", "tinyllama:latest")
LOG_FILE = Path("safety_incidents.jsonl")

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"ignore all instructions",
    r"reveal system prompt",
    r"forget your instructions",
    r"you are now",
    r"pretend you are",
    r"act as",
    r"jailbreak",
    r"do anything now",
    r"bypass",
]

PII_PATTERNS = [
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
    r"\b\d{16}\b",
    r"\b\d{3}-\d{2}-\d{4}\b",
]


def log_incident(rule, input_text, decision):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "rule": rule,
        "redacted_input": input_text[:100] + "...",
        "decision": decision
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[InputGuard] Incident logged: {rule} -> {decision}")


def check_injection(text):
    text_lower = text.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True, pattern
    return False, None


def check_pii(text):
    for pattern in PII_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return True, match.group()
    return False, None


def llm_safety_check(text):
    prompt = f"""You are a safety filter for an educational web dev assistant.
Is this message safe and appropriate for an educational platform?
Reply with JSON only: {{"safe": true, "reason": "message is fine"}}

Message: {text}

JSON:"""

    try:
        response = ollama.chat(
            model=JUDGE_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = response["message"]["content"].strip()
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start != -1 and end > start:
            data = json.loads(raw[start:end])
            return data.get("safe", True), data.get("reason", "")
        return True, "could not parse"
    except:
        return True, "llm check failed, defaulting to safe"


def check(user_input: str) -> dict:
    print(f"\n[InputGuard] Checking input: '{user_input[:60]}...'")

    # check 1 - prompt injection
    injected, pattern = check_injection(user_input)
    if injected:
        log_incident("prompt_injection", user_input, "rejected")
        return {
            "allowed": False,
            "reason": f"Prompt injection detected: '{pattern}'",
            "cleaned_input": None
        }

    # check 2 - PII detection
    has_pii, pii_value = check_pii(user_input)
    if has_pii:
        cleaned = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[EMAIL]", user_input)
        cleaned = re.sub(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "[PHONE]", cleaned)
        cleaned = re.sub(r"\b\d{16}\b", "[CARD]", cleaned)
        log_incident("pii_detected", user_input, "redacted")
        return {
            "allowed": True,
            "reason": "PII detected and redacted",
            "cleaned_input": cleaned
        }

    # check 3 - LLM safety check
    safe, reason = llm_safety_check(user_input)
    if not safe:
        log_incident("llm_safety_check", user_input, "rejected")
        return {
            "allowed": False,
            "reason": f"LLM safety check failed: {reason}",
            "cleaned_input": None
        }

    print(f"[InputGuard] Input is clean, passing through")
    return {
        "allowed": True,
        "reason": "all checks passed",
        "cleaned_input": user_input
    }