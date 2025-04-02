from typing import List, Optional
from sqlalchemy.orm import Session

from app.repository.base_repository import BaseRepository
from app.models.resume import (
    PersonalInfoDB,
    PersonalInfoCreate,
    PersonalInfoUpdate,
    EducationDB,
    ExperienceDB,
    SkillDB,
)


class PersonalInfoRepository(
    BaseRepository[PersonalInfoDB, PersonalInfoCreate, PersonalInfoUpdate]
):
    def get_first(self, db: Session) -> Optional[PersonalInfoDB]:
        """Get the first personal info record (should be only one)"""
        return db.query(self.model).first()


class EducationRepository(BaseRepository[EducationDB, dict, dict]):
    pass


class ExperienceRepository(BaseRepository[ExperienceDB, dict, dict]):
    def get_current_positions(self, db: Session) -> List[ExperienceDB]:
        """Get all current positions"""
        return db.query(self.model).filter(self.model.is_current is True).all()


class SkillRepository(BaseRepository[SkillDB, dict, dict]):
    def get_by_category(self, db: Session, category: str) -> List[SkillDB]:
        """Get skills by category"""
        return db.query(self.model).filter(self.model.category == category).all()


# Create instances
personal_info_repository = PersonalInfoRepository(PersonalInfoDB)
education_repository = EducationRepository(EducationDB)
experience_repository = ExperienceRepository(ExperienceDB)
skill_repository = SkillRepository(SkillDB)
