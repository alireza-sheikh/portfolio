import logging
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.base_model import Base
from app.repository.database import engine, SessionLocal
from app.models.article import ArticleDB
from app.models.resume import PersonalInfoDB, EducationDB, ExperienceDB, SkillDB

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db() -> None:
    """Initialize the database with tables and sample data."""
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")

        # Check if we need to seed data
        db = SessionLocal()
        try:
            # Only seed if the database is empty
            if db.query(PersonalInfoDB).count() == 0:
                seed_sample_data(db)
                logger.info("Sample data seeded successfully")
            else:
                logger.info("Database already contains data, skipping seed")
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise

def seed_sample_data(db: Session) -> None:
    """Seed the database with sample data for development and testing."""
    logger.info("Seeding database with sample data...")

    # Sample personal info
    personal_info = PersonalInfoDB(
        name="John Doe",
        title="Senior Backend Developer",
        email="john.doe@example.com",
        phone="+1 (555) 123-4567",
        location="San Francisco, CA",
        about="Experienced developer with a passion for backend technologies, databases, and containerization.",
        linkedin="https://linkedin.com/in/johndoe",
        github="https://github.com/johndoe",
    )
    db.add(personal_info)

    # Sample education
    education1 = EducationDB(
        institution="University of Technology",
        degree="Bachelor of Science",
        field="Computer Science",
        start_date="2010-09-01",
        end_date="2014-06-01",
        description="Specialized in distributed systems and database technologies.",
    )
    db.add(education1)

    # Sample experience
    experience1 = ExperienceDB(
        company="Tech Solutions Inc.",
        position="Senior Backend Developer",
        start_date="2018-03-01",
        is_current=True,
        description="Developing and maintaining high-performance backend services using FastAPI, PostgreSQL, and Docker.",
    )
    db.add(experience1)

    experience2 = ExperienceDB(
        company="Software Innovations LLC",
        position="Backend Developer",
        start_date="2014-07-01",
        end_date="2018-02-28",
        description="Designed and implemented REST APIs, database schemas, and microservices.",
    )
    db.add(experience2)

    # Sample skills
    skills = [
        SkillDB(name="Python", category="Programming", level=9),
        SkillDB(name="FastAPI", category="Framework", level=8),
        SkillDB(name="PostgreSQL", category="Database", level=8),
        SkillDB(name="Docker", category="DevOps", level=7),
        SkillDB(name="Kubernetes", category="DevOps", level=6),
        SkillDB(name="Redis", category="Database", level=7),
    ]
    for skill in skills:
        db.add(skill)

    # Sample article
    article = ArticleDB(
        title="Getting Started with FastAPI",
        slug="getting-started-with-fastapi",
        content="""
        # Getting Started with FastAPI

        FastAPI is a modern, fast (high-performance), web framework for
        building APIs with Python 3.7+ based on standard Python type hints.

        ## Key Features

        - **Fast**: Very high performance, on par with NodeJS and Go
        - **Fast to code**: Increase the speed to develop features by about 200% to 300%
        - **Fewer bugs**: Reduce about 40% of human (developer) induced errors
        - **Intuitive**: Great editor support. Completion everywhere. Less time debugging
        - **Easy**: Designed to be easy to use and learn. Less time reading docs
        - **Short**: Minimize code duplication. Multiple features from each parameter
            declaration

        ## Installation

        pip install fastapi
        pip install uvicorn

        ## Example

        from fastapi import FastAPI

        app = FastAPI()

        @app.get("/")
        def read_root():
            return {"Hello": "World"}

        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: str = None):
            return {"item_id": item_id, "q": q}

        Run the server:

        uvicorn main:app --reload
""",
        summary="A quick introduction to using FastAPI for building high-performance APIs",
        is_published=True,
    )
    db.add(article)

    # Commit all sample data
    db.commit()

