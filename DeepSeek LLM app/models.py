from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    model: str = "deepseek-chat"  # Default model