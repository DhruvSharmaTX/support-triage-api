from fastapi import APIRouter
from app.services.groq_service import GroqService
from app.core.config import GROQ_MODEL

router = APIRouter(prefix="/model", tags=["Model"])
@router.get("/status")
def model_status():
    try:
        groq = GroqService()
        groq.llm.invoke("Hello")
        return {
            "provider": "LangChain+Groq",
            "model": GROQ_MODEL,
            "status": "available",
        }
    except Exception as e:
        return {
            "provider": "LangChain+Groq",
            "model": GROQ_MODEL,
            "status": "unavailable",
            "error": str(e),
        }
