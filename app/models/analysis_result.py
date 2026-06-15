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
    reasoning = Column(Text)
