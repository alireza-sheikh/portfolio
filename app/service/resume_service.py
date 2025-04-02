from typing import List, Optional, Dict
from sqlalchemy.orm import Session

from app.repository.resume_repository import (
    personal_info_repository,
    education_repository,
    experience_repository,
    skill_repository,
)
from app.models.resume import PersonalInfo, Education, Experience, Skill, ResumeResponse


class ResumeService:
    def get_personal_info(self, db: Session) -> Optional[PersonalInfo]:
        db_obj = personal_info_repository.get_first(db=db)
        if db_obj:
            return PersonalInfo.from_orm(db_obj)
        return None

    def get_education(self, db: Session) -> List[Education]:
        db_objs = education_repository.get_multi(db=db)
        return [Education.from_orm(obj) for obj in db_objs]

    def get_experience(self, db: Session) -> List[Experience]:
        db_objs = experience_repository.get_multi(db=db)
        return [Experience.from_orm(obj) for obj in db_objs]

    def get_skills(self, db: Session) -> List[Skill]:
        db_objs = skill_repository.get_multi(db=db)
        return [Skill.from_orm(obj) for obj in db_objs]

    def get_resume(self, db: Session) -> ResumeResponse:
        """Get the complete resume with all sections"""
        return ResumeResponse(
            personal_info=self.get_personal_info(db),
            education=self.get_education(db),
            experience=self.get_experience(db),
            skills=self.get_skills(db),
        )


resume_service = ResumeService()
