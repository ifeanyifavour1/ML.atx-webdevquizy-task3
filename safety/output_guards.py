import re
import json
import ollama
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

judge = os.getenv("JUDGE_MODEL", "tinyllama:latest")
log_path = Path("safety_incidents.jsonl")

# patterns to catch common PII
pii_patterns = [
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",  # email
    r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",                 # phone
    r"\b\d{16}\b",                                          # credit card
    r"\b\d{3}-\d{2}-\d{4}\b",                              # SSN
]


def save_incident(rule, text, decision):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "rule": rule,
        "redacted_input": text[:100] + "...",
        "decision": decision
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[OutputGuard] logged: {rule} -> {decision}")


def remove_pii(text):
    found = False
    result = text
    for p in pii_patterns:
        if re.search(p, result):
            found = True
            result = re.sub(p, "[REDACTED]", result)
    return found, result


def is_grounded(answer, chunks):
    # use tinyllama to check if answer actually came from the chunks
    context = str([c["chunk"]["text"][:200] for c in chunks[:2]])
    prompt = f"""Check if this answer is based on the context below.
Answer: {answer[:400]}
Context: {context}
Reply with JSON only: {{"grounded": true, "reason": "explain why"}}
JSON:"""

    try:
        resp = ollama.chat(
            model=judge,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = resp["message"]["content"].strip()
        s = raw.find("{")
        e = raw.rfind("}") + 1
        if s != -1 and e > s:
            data = json.loads(raw[s:e])
            return data.get("grounded", True), data.get("reason", "")
        return True, "parse failed"
    except:
        return True, "check failed"


def check(answer: str, chunks: list) -> dict:
    print("\n[OutputGuard] running output checks...")

    # first remove any PII that snuck into the answer
    has_pii, clean = remove_pii(answer)
    if has_pii:
        save_incident("pii_in_output", answer, "redacted")
        answer = clean

    # then check if the answer is actually grounded in the docs
    grounded, reason = is_grounded(answer, chunks)
    if not grounded:
        save_incident("not_grounded", answer, "flagged")
        answer = answer + "\n\n⚠️ Warning: answer may not be fully supported by documents."

    print("[OutputGuard] done")
    return {
        "answer": answer,
        "pii_found": has_pii,
        "grounded": grounded
    }