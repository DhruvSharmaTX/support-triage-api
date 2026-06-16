from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.ticket_schema import TicketRequest, TicketAnalysisResponse
from app.services.similarity_service import analyze_ticket
from app.repositories.analysis_repository import save_analysis_result
from app.repositories.history_repository import get_analysis_history
from app.schemas.history_schema import HistoryResponse
from typing import List

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/analyze", response_model=TicketAnalysisResponse)
def analyze(request: TicketRequest, db: Session = Depends(get_db)):
    result = analyze_ticket(request.title, request.description)
    save_analysis_result(db, request.title, request.description, result)
    return result

@router.get("/history", response_model=List[HistoryResponse])
def history(db: Session = Depends(get_db)):
    return get_analysis_history(db)
