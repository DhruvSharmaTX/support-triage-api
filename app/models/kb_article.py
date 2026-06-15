from sqlalchemy import Column, String, Text
from app.core.database import Base
class KBArticle(Base):
    __tablename__ = "kb_articles"
    article_id = Column(String(20), primary_key=True)
    title = Column(Text)
    body = Column(Text)
    category = Column(String(50))
    tags = Column(Text)
    status = Column(String(20))
