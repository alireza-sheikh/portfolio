from typing import List
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import db_dependency
from app.models.article import Article, ArticleCreate
from app.service.article_service import article_service

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/", response_model=List[Article])
def get_articles(skip: int = 0, limit: int = 10, db: Session = db_dependency):
    """Get all published articles"""
    articles = article_service.get_published_articles(db=db, skip=skip, limit=limit)
    return articles


@router.get("/{slug}", response_model=Article)
def get_article(slug: str, db: Session = db_dependency):
    """Get a specific article by slug"""
    article = article_service.get_by_slug(db=db, slug=slug)
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found"
        )
    return article


@router.post("/", response_model=Article, status_code=status.HTTP_201_CREATED)
def create_article(article_in: ArticleCreate, db: Session = db_dependency):
    """Create a new article"""
    return article_service.create_article(db=db, article_in=article_in)
