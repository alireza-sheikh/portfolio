from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import db_dependency
from app.models.resume import PersonalInfo, Education, Experience, Skill, ResumeResponse
from app.service.resume_service import resume_service

router = APIRouter(prefix="/resume", tags=["resume"])

@router.get("/", response_model=ResumeResponse)
def get_resume(db: Session = db_dependency):
    """Get the complete resume"""
    return resume_service.get_resume(db=db)

@router.get("/personal-info", response_model=PersonalInfo)
def get_personal_info(db: Session = db_dependency):
    """Get personal information"""
    personal_info = resume_service.get_personal_info(db=db)
    if not personal_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Personal information not found"
        )
    return personal_info