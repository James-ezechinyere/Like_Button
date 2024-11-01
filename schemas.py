from pydantic import BaseModel

# Pydantic models for request validation
class ArticleLikeRequest(BaseModel):
    articleId: str