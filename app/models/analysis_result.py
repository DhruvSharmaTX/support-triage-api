from sqlalchemy import Column, Integer, Float, Text, String
from app.core.database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    description = Column(Text)
    predicted_category = Column(String(50))
    predicted_priority = Column(String(20))
    confidence = Column(Float)
    similar_ticket_id = Column(String(20))
    recommended_articles = Column(Text)
    reasoning = Column(Text)
    suggested_resolution = Column(Text)
