from typing import List, Optional
from sqlalchemy.orm import Session

from app.repository.base_repository import BaseRepository
from app.models.article import ArticleDB, ArticleCreate, ArticleUpdate


class ArticleRepository(BaseRepository[ArticleDB, ArticleCreate, ArticleUpdate]):
    def get_by_slug(self, db: Session, slug: str) -> Optional[ArticleDB]:
        return db.query(self.model).filter(self.model.slug == slug).first()

    def get_published(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ArticleDB]:
        return (
            db.query(self.model)
            .filter(self.model.is_published is True)
            .offset(skip)
            .limit(limit)
            .all()
        )


article_repository = ArticleRepository(ArticleDB)
