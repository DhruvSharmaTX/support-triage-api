from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.analytics_repository import get_analytics_summary

router = APIRouter(prefix="/analytics", tags=["Analytics"])
@router.get("/summary")
def analytics_summary(db: Session = Depends(get_db)):
    return get_analytics_summary(db)
