from pydantic import BaseModel, ConfigDict

class HistoryResponse(BaseModel):
    id: int
    title: str
    predicted_category: str
    predicted_priority: str
    confidence: float
    model_config = ConfigDict(from_attributes=True)
