from app.schemas import DiagramRequest
from .token_utils import count_tokens
import logging

logger = logging.getLogger(__name__)

def generate_diagram_code(data: DiagramRequest) -> dict:
    token_count = count_tokens(data.description)
    logger.info(f"Generating {data.model_type} diagram with {token_count} tokens.")

    # TODO: Replace mock with Langchain integration
    code = f"// Mockowany diagram ({data.model_type})\n// Tokeny: {token_count}\n[START] {data.description} [END]"

    return {
        "diagram_code": code,
        "format": data.style
    }