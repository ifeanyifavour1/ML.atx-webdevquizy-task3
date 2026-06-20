import json
from pathlib import Path
from datetime import datetime
from agents.schemas import RetrievalRequest, SynthesisRequest
from agents import retriever_agent, synthesizer, safety_reviewer

TRACE_FILE = Path("traces.jsonl")
MAX_ROUNDS = 2


def log_trace(entry):
    with open(TRACE_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def run(query: str, user_role: str = "student") -> dict:
    print(f"\n{'='*60}")
    print(f"[Orchestrator] New request: '{query}'")
    print(f"[Orchestrator] User role: {user_role}")
    print(f"{'='*60}")

    trace = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "user_role": user_role,
        "messages": []
    }

    # step 1 - send retrieval request
    retrieval_req = RetrievalRequest(
        sender="orchestrator",
        recipient="retriever_agent",
        query=query
    )
    trace["messages"].append({
        "from": "orchestrator",
        "to": "retriever_agent",
        "type": "RetrievalRequest",
        "query": query
    })
    log_trace({"event": "retrieval_request", "query": query})

    # step 2 - get chunks from retriever
    retrieval_result = retriever_agent.run(retrieval_req)
    trace["messages"].append({
        "from": "retriever_agent",
        "to": "orchestrator",
        "type": "RetrievalResult",
        "chunks_found": len(retrieval_result.chunks)
    })
    log_trace({"event": "retrieval_result", "chunks": len(retrieval_result.chunks)})

    if not retrieval_result.chunks:
        return {
            "answer": "I don't have enough information on that topic.",
            "citations": [],
            "trace": trace
        }

    # step 3 - send to synthesizer
    rounds = 0
    final_answer = None
    critique = ""

    while rounds < MAX_ROUNDS:
        rounds += 1
        print(f"\n[Orchestrator] Synthesis round {rounds}")

        synth_req = SynthesisRequest(
            sender="orchestrator",
            recipient="synthesizer",
            query=query + (f"\n\nPrevious answer was rejected. Critique: {critique}" if critique else ""),
            chunks=retrieval_result.chunks
        )
        trace["messages"].append({
            "from": "orchestrator",
            "to": "synthesizer",
            "type": "SynthesisRequest",
            "round": rounds
        })

        synth_result = synthesizer.run(synth_req)
        trace["messages"].append({
            "from": "synthesizer",
            "to": "orchestrator",
            "type": "SynthesisResult",
            "answer_length": len(synth_result.answer)
        })
        log_trace({"event": "synthesis_result", "round": rounds})

        # step 4 - safety review
        verdict = safety_reviewer.run(synth_result)
        trace["messages"].append({
            "from": "safety_reviewer",
            "to": "orchestrator",
            "type": "SafetyVerdict",
            "approved": verdict.approved,
            "reason": verdict.reason
        })
        log_trace({"event": "safety_verdict", "approved": verdict.approved})

        if verdict.approved:
            final_answer = synth_result.answer
            break
        else:
            critique = verdict.reason
            print(f"[Orchestrator] Answer rejected, retrying... Reason: {critique}")

    if not final_answer:
        final_answer = "I was unable to generate a safe answer for your question."

    trace["final_answer"] = final_answer
    trace["citations"] = synth_result.citations
    trace["rounds"] = rounds

    log_trace({"event": "final_answer", "rounds": rounds, "query": query})

    return {
        "answer": final_answer,
        "citations": synth_result.citations,
        "trace": trace
    }