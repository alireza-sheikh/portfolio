from fastapi import APIRouter

from app.api.routes import health, resume, articles

router = APIRouter()
router.include_router(health.router)
router.include_router(resume.router)
router.include_router(articles.router)
