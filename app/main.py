from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import health

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

# Include routers
app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])

# Mount static files directory
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
async def root():
    return {"message": "Welcome to my personal website API"}
