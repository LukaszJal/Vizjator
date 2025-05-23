from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.schemas import DiagramRequest, DiagramResponse
from app.services.llm_service import generate_diagram_code
import logging

app = FastAPI(title="Vizjator Backend")

# TODO: Add CORS and Auth Middleware here

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vizjator")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Wewnętrzny błąd serwera"}
    )

@app.post("/generate-diagram", response_model=DiagramResponse)
def generate_diagram(request: DiagramRequest):
    try:
        return generate_diagram_code(request)
    except Exception as e:
        logger.exception("Error during diagram generation")
        raise