import os
import json
import pickle
from pathlib import Path
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
from dotenv import load_dotenv

load_dotenv()

INDEX_DIR = Path("index")
TOP_K = int(os.getenv("TOP_K", 5))
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

model = None
index = None
bm25 = None
chunks = None


def load_index():
    global model, index, bm25, chunks
    if model is not None:
        return
    print("Loading indexes...")
    model = SentenceTransformer(EMBED_MODEL)
    index = faiss.read_index(str(INDEX_DIR / "faiss.index"))
    with open(INDEX_DIR / "bm25.pkl", "rb") as f:
        bm25 = pickle.load(f)
    with open(INDEX_DIR / "chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)
    print("Indexes loaded!")


def dense_search(query, k=TOP_K):
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)
    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(chunks):
            results.append({
                "chunk": chunks[idx],
                "dense_score": float(1 / (1 + distances[0][i]))
            })
    return results


def bm25_search(query, k=TOP_K):
    tokens = query.lower().split()
    scores = bm25.get_scores(tokens)
    top_indices = np.argsort(scores)[::-1][:k]
    results = []
    for idx in top_indices:
        results.append({
            "chunk": chunks[idx],
            "bm25_score": float(scores[idx])
        })
    return results


def hybrid_search(query, k=TOP_K):
    load_index()
    dense = dense_search(query, k)
    sparse = bm25_search(query, k)

    scores = {}
    for rank, item in enumerate(dense):
        cid = item["chunk"]["chunk_id"]
        scores[cid] = scores.get(cid, 0) + 1 / (rank + 1)

    for rank, item in enumerate(sparse):
        cid = item["chunk"]["chunk_id"]
        scores[cid] = scores.get(cid, 0) + 1 / (rank + 1)

    all_chunks = {i["chunk"]["chunk_id"]: i["chunk"] for i in dense + sparse}
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]

    results = []
    for cid, score in ranked:
        results.append({
            "chunk": all_chunks[cid],
            "hybrid_score": round(score, 4)
        })
    return results


if __name__ == "__main__":
    results = hybrid_search("What is the CSS box model?")
    for r in results:
        print(f"\nChunk: {r['chunk']['chunk_id']} | Score: {r['hybrid_score']}")
        print(r['chunk']['text'][:200])