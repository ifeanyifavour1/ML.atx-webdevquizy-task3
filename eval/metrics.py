import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from pathlib import Path
from rag.retriever import hybrid_search

golden_set = json.loads(Path("eval/golden_set.json").read_text())


def recall_at_k(retrieved_ids, expected_ids, k=5):
    top_k = retrieved_ids[:k]
    hits = [e for e in expected_ids if e in top_k]
    return len(hits) / len(expected_ids) if expected_ids else 0


def mean_reciprocal_rank(retrieved_ids, expected_ids):
    for rank, rid in enumerate(retrieved_ids, start=1):
        if rid in expected_ids:
            return 1 / rank
    return 0


def run_eval():
    print("Running retrieval eval on golden set...\n")
    recall_scores = []
    mrr_scores = []

    for item in golden_set:
        question = item["question"]
        expected = item["expected_chunk_ids"]

        results = hybrid_search(question)
        retrieved_ids = [r["chunk"]["chunk_id"] for r in results]

        r5 = recall_at_k(retrieved_ids, expected)
        mrr = mean_reciprocal_rank(retrieved_ids, expected)

        recall_scores.append(r5)
        mrr_scores.append(mrr)

        print(f"Q: {question[:50]}")
        print(f"   Expected: {expected}")
        print(f"   Retrieved: {retrieved_ids[:3]}")
        print(f"   Recall@5: {r5} | MRR: {round(mrr, 3)}\n")

    avg_recall = round(sum(recall_scores) / len(recall_scores), 3)
    avg_mrr = round(sum(mrr_scores) / len(mrr_scores), 3)

    print(f"{'='*50}")
    print(f"Average Recall@5: {avg_recall}")
    print(f"Average MRR:      {avg_mrr}")
    print(f"{'='*50}")

    return avg_recall, avg_mrr


if __name__ == "__main__":
    run_eval()