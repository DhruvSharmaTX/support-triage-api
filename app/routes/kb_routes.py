from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.kb_repository import search_kb_articles
from app.schemas.kb_schema import KBArticleResponse

router = APIRouter(prefix="/kb", tags=["Knowledge Base"])

@router.get("/search", response_model=List[KBArticleResponse])
def kb_search(query: str, db: Session = Depends(get_db)):
    return search_kb_articles(db, query)
