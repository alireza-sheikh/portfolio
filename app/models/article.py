from sqlalchemy import Column, String, Text, Boolean
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.models.base_model import BaseModel as DBBaseModel


# Database Model
class ArticleDB(DBBaseModel):
    __tablename__ = "articles"

    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), nullable=False, unique=True, index=True)
    content = Column(Text, nullable=False)
    summary = Column(String(500))
    is_published = Column(Boolean, default=False)


# Pydantic Schemas
class ArticleBase(BaseModel):
    title: str
    slug: str
    content: str
    summary: Optional[str] = None
    is_published: bool = False


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    is_published: Optional[bool] = None


class Article(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
