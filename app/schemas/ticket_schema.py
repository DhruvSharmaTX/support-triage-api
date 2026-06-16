from pydantic import BaseModel

class TicketRequest(BaseModel):
    title: str
    description: str
    channel: str
    requester_type: str
class SimilarTicket(BaseModel):
    ticket_id: str
    title: str
class RecommendedArticle(BaseModel):
    article_id: str
    title: str
    category: str
    similarity: float
class TicketAnalysisResponse(BaseModel):
    predicted_category: str
    predicted_priority: str
    confidence: float
    reasoning: str
    suggested_resolution: str
    similar_ticket: SimilarTicket
    recommended_articles: list[RecommendedArticle]
