from sqlalchemy import Column, String, Text, Date, Boolean, Integer
from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel

from app.models.base_model import BaseModel as DBBaseModel


# Database Models
class PersonalInfoDB(DBBaseModel):
    __tablename__ = "personal_info"

    name = Column(String(255), nullable=False)
    title = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    location = Column(String(255))
    about = Column(Text)
    linkedin = Column(String(255))
    github = Column(String(255))


class EducationDB(DBBaseModel):
    __tablename__ = "education"

    institution = Column(String(255), nullable=False)
    degree = Column(String(255))
    field = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text)


class ExperienceDB(DBBaseModel):
    __tablename__ = "experience"

    company = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    is_current = Column(Boolean, default=False)
    description = Column(Text)


class SkillDB(DBBaseModel):
    __tablename__ = "skills"

    name = Column(String(255), nullable=False)
    category = Column(String(255))
    level = Column(Integer)  # 1-10 scale


# Pydantic Schemas
class PersonalInfoBase(BaseModel):
    name: str
    title: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    about: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None


class PersonalInfoCreate(PersonalInfoBase):
    pass


class PersonalInfoUpdate(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    about: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None


class PersonalInfo(PersonalInfoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Education(BaseModel):
    id: int
    institution: str
    degree: Optional[str] = None
    field: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Experience(BaseModel):
    id: int
    company: str
    position: str
    start_date: date
    end_date: Optional[date] = None
    is_current: bool = False
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Skill(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    level: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ResumeResponse(BaseModel):
    personal_info: Optional[PersonalInfo] = None
    education: List[Education] = []
    experience: List[Experience] = []
    skills: List[Skill] = []

    class Config:
        orm_mode = True
