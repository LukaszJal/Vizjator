from pydantic import BaseModel
from typing import Optional

class DiagramRequest(BaseModel):
    description: str
    model_type: str
    target_language: Optional[str] = "PL"
    detail_level: Optional[str] = "medium"
    style: Optional[str] = "plantuml"
    annotations: Optional[bool] = False
    context_id: Optional[str] = None
    user_id: Optional[str] = None

class DiagramResponse(BaseModel):
    diagram_code: str
    format: str