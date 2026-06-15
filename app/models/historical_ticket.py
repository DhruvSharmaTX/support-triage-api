from sqlalchemy import Column, String, Text
from app.core.database import Base
class HistoricalTicket(Base):
    __tablename__ = "historical_tickets"
    ticket_id = Column(String(20), primary_key=True)
    title = Column(Text)
    description = Column(Text)
    category = Column(String(50))
    priority = Column(String(20))
    resolution_summary = Column(Text)
    status = Column(String(20))
    created_at = Column(String(50))
