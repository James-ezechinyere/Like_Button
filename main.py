from fastapi import FastAPI, HTTPException, Depends
from database import *
from sqlalchemy.future import select
from models import Article, Base
from schemas import ArticleLikeRequest
import asyncio

# FastAPI app Initialization
app = FastAPI()

# Async function to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Endpoint to get like count for an article
@app.get("/api/article/like-count")
async def get_like_count(articleId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Article).where(Article.article_id == articleId))
    article = result.scalars().first()
    if not article:
        return {"likes": 0}
    return {"likes": article.like_count}

# Endpoint to increment the like count for an article
@app.post("/api/article/like")
async def like_article(request: ArticleLikeRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Article).where(Article.article_id == request.articleId))
    article = result.scalars().first()
    if not article:
        # If the article does not exist, create it with a starting like count of 1
        article = Article(article_id=request.articleId, like_count=1)
        db.add(article)
    else:
        # Increment the existing like count
        article.like_count += 1
    await db.commit()
    await db.refresh(article)
    return {"likes": article.like_count}
