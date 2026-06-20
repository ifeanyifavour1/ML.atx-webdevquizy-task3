from agents.schemas import RetrievalRequest, RetrievalResult
from rag.retriever import hybrid_search
from rag.reranker import rerank


def run(request: RetrievalRequest) -> RetrievalResult:
    print(f"\n[RetrieverAgent] Got request from {request.sender}")
    print(f"[RetrieverAgent] Searching for: '{request.query}'")

    candidates = hybrid_search(request.query, k=request.top_k)
    reranked = rerank(request.query, candidates)

    print(f"[RetrieverAgent] Found {len(reranked)} chunks")

    return RetrievalResult(
        sender="retriever_agent",
        recipient=request.sender,
        query=request.query,
        chunks=reranked
    )