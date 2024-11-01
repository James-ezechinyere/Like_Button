from sqlalchemy import Column, Integer, String
from database import Base

# Article model for storing like counts
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(String, unique=True, index=True, nullable=False)
    like_count = Column(Integer, default=0)