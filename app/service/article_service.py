from typing import List, Optional
from sqlalchemy.orm import Session

from app.repository.article_repository import article_repository
from app.models.article import Article, ArticleCreate, ArticleUpdate


class ArticleService:
    def get_by_id(self, db: Session, id: int) -> Optional[Article]:
        db_obj = article_repository.get(db=db, id=id)
        if db_obj:
            return Article.model_validate(db_obj)
        return None

    def get_by_slug(self, db: Session, slug: str) -> Optional[Article]:
        db_obj = article_repository.get_by_slug(db=db, slug=slug)
        if db_obj:
            return Article.model_validate(db_obj)
        return None

    def get_published(self, db: Session, skip: int = 0, limit: int = 10) -> List[Article]:
        db_objs = article_repository.get_published(db=db, skip=skip, limit=limit)
        return [Article.model_validate(obj) for obj in db_objs]

    def create(self, db: Session, article_in: ArticleCreate) -> Article:
        db_obj = article_repository.create(db=db, obj_in=article_in)
        return Article.model_validate(db_obj)


article_service = ArticleService()
