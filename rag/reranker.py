import ollama
import os
from dotenv import load_dotenv

load_dotenv()

SOLVER_MODEL = os.getenv("SOLVER_MODEL", "llama3.2:1b")


def rerank(query, candidates):
    if not candidates:
        return candidates

    print(f"Reranking {len(candidates)} candidates...")
    scores = []

    for item in candidates:
        chunk_text = item["chunk"]["text"][:300]
        prompt = f"""Rate how relevant this text is for answering the question.
Question: {query}
Text: {chunk_text}
Reply with just a number from 0 to 10. Nothing else."""

        try:
            response = ollama.chat(
                model=SOLVER_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            score_text = response["message"]["content"].strip()
            score = float(''.join(c for c in score_text if c.isdigit() or c == '.'))
            if score > 10:
                score = 10.0
        except:
            score = 5.0

        scores.append({
            "chunk": item["chunk"],
            "hybrid_score": item.get("hybrid_score", 0),
            "rerank_score": round(score, 2)
        })

    reranked = sorted(scores, key=lambda x: x["rerank_score"], reverse=True)

    print("Scores before vs after reranking:")
    for i, item in enumerate(reranked):
        print(f"  {item['chunk']['chunk_id']} | hybrid: {item['hybrid_score']} | rerank: {item['rerank_score']}")

    return reranked


if __name__ == "__main__":
    from retriever import hybrid_search
    query = "What is the CSS box model?"
    candidates = hybrid_search(query)
    reranked = rerank(query, candidates)
    print("\nTop result after reranking:")
    print(reranked[0]["chunk"]["text"][:300])