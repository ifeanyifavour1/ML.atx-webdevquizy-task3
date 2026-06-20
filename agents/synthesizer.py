import ollama
import os
from dotenv import load_dotenv
from agents.schemas import SynthesisRequest, SynthesisResult

load_dotenv()

SOLVER_MODEL = os.getenv("SOLVER_MODEL", "llama3.2:1b")


def run(request: SynthesisRequest) -> SynthesisResult:
    print(f"\n[Synthesizer] Got request from {request.sender}")
    print(f"[Synthesizer] Generating answer for: '{request.query}'")

    context = ""
    citations = []
    for i, item in enumerate(request.chunks[:3]):
        chunk = item["chunk"]
        context += f"\n[{chunk['chunk_id']}]:\n{chunk['text'][:400]}\n"
        citations.append(chunk["chunk_id"])

    prompt = f"""You are a web development teaching assistant for ATX WebDevQuizy.
Answer the question using ONLY the context below.
If the context does not contain enough information, say "I don't have enough information on that topic."
Always mention which chunk ID your answer comes from.

Context:
{context}

Question: {request.query}

Answer:"""

  

    response = ollama.chat(
        model=SOLVER_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"].strip()
    print(f"[Synthesizer] Answer generated ({len(answer)} chars)")

    return SynthesisResult(
        sender="synthesizer",
        recipient=request.sender,
        query=request.query,
        answer=answer,
        citations=citations
    )