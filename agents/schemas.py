from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid


class RetrievalRequest(BaseModel):
    message_id: str = ""
    sender: str = "orchestrator"
    recipient: str = "retriever_agent"
    query: str
    top_k: int = 5
    timestamp: str = ""

    def __init__(self, **data):
        super().__init__(**data)
        if not self.message_id:
            self.message_id = str(uuid.uuid4())[:8]
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class RetrievalResult(BaseModel):
    message_id: str = ""
    sender: str = "retriever_agent"
    recipient: str = "orchestrator"
    query: str
    chunks: List[dict]
    timestamp: str = ""

    def __init__(self, **data):
        super().__init__(**data)
        if not self.message_id:
            self.message_id = str(uuid.uuid4())[:8]
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class SynthesisRequest(BaseModel):
    message_id: str = ""
    sender: str = "orchestrator"
    recipient: str = "synthesizer"
    query: str
    chunks: List[dict]
    timestamp: str = ""

    def __init__(self, **data):
        super().__init__(**data)
        if not self.message_id:
            self.message_id = str(uuid.uuid4())[:8]
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class SynthesisResult(BaseModel):
    message_id: str = ""
    sender: str = "synthesizer"
    recipient: str = "orchestrator"
    query: str
    answer: str
    citations: List[str]
    timestamp: str = ""

    def __init__(self, **data):
        super().__init__(**data)
        if not self.message_id:
            self.message_id = str(uuid.uuid4())[:8]
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class SafetyVerdict(BaseModel):
    message_id: str = ""
    sender: str = "safety_reviewer"
    recipient: str = "orchestrator"
    approved: bool
    reason: str
    cleaned_answer: Optional[str] = None
    timestamp: str = ""

    def __init__(self, **data):
        super().__init__(**data)
        if not self.message_id:
            self.message_id = str(uuid.uuid4())[:8]
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()