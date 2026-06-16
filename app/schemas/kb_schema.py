from pydantic import BaseModel, ConfigDict

class KBArticleResponse(BaseModel):
    article_id: str
    title: str
    category: str
    status: str
    model_config=ConfigDict(from_attributes=True)
