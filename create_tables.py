from app.core.database import engine
from app.models.kb_article import KBArticle
from app.models.historical_ticket import HistoricalTicket
from app.models.analysis_result import AnalysisResult
from app.core.database import Base
Base.metadata.create_all(bind=engine)
print("Tables Created Successfully")
