from fastapi import APIRouter
from sqlalchemy import text
from app.core.database import SessionLocal
from app.models.kb_article import KBArticle
from app.models.historical_ticket import HistoricalTicket
router = APIRouter()
@router.get("/health")
def health_check():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        kb_count = db.query(KBArticle).count()
        ticket_count = db.query(HistoricalTicket).count()
        return {
            "status": "healthy",
            "database": "connection",
            "kb_articles": kb_count,
            "historical_tickets": ticket_count,
        }
    finally:
        db.close()