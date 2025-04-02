from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

from app.core.config import settings
from app.api.routes import health, articles, resume  # Import individual routers
from app.repository.init_db import init_db

# Create FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A personal website showcasing resume and articles",
    version="0.1.0",
)

# Set up CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Initialize database
@app.on_event("startup")
async def startup_event():
    init_db()


# Include routers directly
app.include_router(health.router, prefix=settings.API_V1_STR)
app.include_router(articles.router, prefix=settings.API_V1_STR)
app.include_router(resume.router, prefix=settings.API_V1_STR)

# Mount static files directory
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="frontend/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Personal Website"}
    )
