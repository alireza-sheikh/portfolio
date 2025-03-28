from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings
from app.api.routes import articles, resume

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A personal website showcasing resume and articles",
    version="0.1.0",
)

# Include routers
app.include_router(articles.router, prefix=settings.API_V1_STR, tags=["articles"])
app.include_router(resume.router, prefix=settings.API_V1_STR, tags=["resume"])

# Mount static files directory
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="frontend/templates")


@app.get("/")
async def root():
    return {"message": "Welcome to my personal website API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
