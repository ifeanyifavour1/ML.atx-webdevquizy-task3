import ollama
import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from agents.schemas import SynthesisResult, SafetyVerdict

load_dotenv()

JUDGE_MODEL = os.getenv("JUDGE_MODEL", "tinyllama:latest")
LOG_FILE = Path("safety_incidents.jsonl")


def log_incident(rule, input_text, decision):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "rule": rule,
        "redacted_input": input_text[:100] + "...",
        "decision": decision
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[SafetyReviewer] Incident logged: {rule}")


def run(result: SynthesisResult) -> SafetyVerdict:
    print(f"\n[SafetyReviewer] Reviewing answer from {result.sender}")

    # TEMP: force a rejection on first call to test the feedback loop
    if os.getenv("FORCE_REJECT_ONCE") == "1":
        os.environ["FORCE_REJECT_ONCE"] = "0"
        log_incident("safety_reviewer_rejection", result.answer, "rejected")
        print("[SafetyReviewer] Verdict: REJECTED — TEST: forcing rejection to verify retry loop")
        return SafetyVerdict(
            sender="safety_reviewer",
            recipient="orchestrator",
            approved=False,
            reason="TEST: forcing rejection to verify retry loop",
            cleaned_answer=None
        )

    prompt = f"""You are a safety reviewer for an educational web dev assistant.
Check if this answer is appropriate and safe for students.
Reply with JSON only like this: {{"approved": true, "reason": "answer is fine"}}

Question: {result.query}
Answer: {result.answer[:500]}

JSON response:"""

    try:
        response = ollama.chat(
            model=JUDGE_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        text = response["message"]["content"].strip()
        start = text.find("{")
        end = text.rfind("}") + 1
        if start != -1 and end > start:
            data = json.loads(text[start:end])
            approved = data.get("approved", True)
            reason = data.get("reason", "no reason given")
        else:
            approved = True
            reason = "could not parse verdict, defaulting to approved"
    except Exception as e:
        approved = True
        reason = f"reviewer error: {str(e)}"

    if not approved:
        log_incident("safety_reviewer_rejection", result.answer, "rejected")

    print(f"[SafetyReviewer] Verdict: {'APPROVED' if approved else 'REJECTED'} — {reason}")

    return SafetyVerdict(
        sender="safety_reviewer",
        recipient="orchestrator",
        approved=approved,
        reason=reason,
        cleaned_answer=result.answer if approved else None
    )