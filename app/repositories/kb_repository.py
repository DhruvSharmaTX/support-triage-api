from app.models.kb_article import KBArticle


def search_kb_articles(db, query: str):
    return db.query(KBArticle).filter(KBArticle.title.ilike(f"%{query}%")).all()
