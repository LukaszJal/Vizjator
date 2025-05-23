import tiktoken
from app.config import LLM_MODEL

def count_tokens(text: str, model: str = LLM_MODEL) -> int:
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))