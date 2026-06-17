import os
import json
import pickle
from pathlib import Path
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from rank_bm25 import BM25Okapi

load_dotenv()

CORPUS_DIR = Path("corpus")
INDEX_DIR = Path("index")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 400))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")


def load_documents():
    docs = []
    for file in sorted(CORPUS_DIR.glob("*.md")):
        text = file.read_text(encoding="utf-8")
        lines = text.strip().split("\n")
        doc_id = file.stem
        topic = "general"
        for line in lines:
            if line.startswith("topic:"):
                topic = line.split(":", 1)[1].strip()
                break
        docs.append({
            "doc_id": doc_id,
            "topic": topic,
            "text": text,
            "source": file.name
        })
    print(f"Loaded {len(docs)} documents")
    return docs


def chunk_documents(docs):
    chunks = []
    chunk_id = 0
    for doc in docs:
        text = doc["text"]
        words = text.split()
        start = 0
        while start < len(words):
            end = start + CHUNK_SIZE
            chunk_text = " ".join(words[start:end])
            chunks.append({
                "chunk_id": f"{doc['doc_id']}_chunk{chunk_id}",
                "doc_id": doc["doc_id"],
                "topic": doc["topic"],
                "source": doc["source"],
                "text": chunk_text
            })
            chunk_id += 1
            start += CHUNK_SIZE - CHUNK_OVERLAP
    print(f"Created {len(chunks)} chunks from {len(docs)} documents")
    return chunks


def build_index(chunks):
    INDEX_DIR.mkdir(exist_ok=True)
    print("Loading embedding model...")
    model = SentenceTransformer(EMBED_MODEL)
    texts = [c["text"] for c in chunks]
    print("Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, str(INDEX_DIR / "faiss.index"))
    tokenized = [t.lower().split() for t in texts]
    bm25 = BM25Okapi(tokenized)
    with open(INDEX_DIR / "bm25.pkl", "wb") as f:
        pickle.dump(bm25, f)
    with open(INDEX_DIR / "chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)
    print(f"Index built and saved to {INDEX_DIR}/")
    return index, bm25, chunks


def ingest():
    docs = load_documents()
    chunks = chunk_documents(docs)
    index, bm25, chunks = build_index(chunks)
    return index, bm25, chunks


if __name__ == "__main__":
    ingest()
    print("Ingestion complete!")