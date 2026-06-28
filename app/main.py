from fastapi import FastAPI

from app.core.settings import settings

from app.database.db import Base, engine
import app.database.models

from app.api.health import router as health_router
from app.api.story import router as story_router
from app.api.project import router as project_router

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

# Register API routers
app.include_router(health_router)
app.include_router(story_router)
app.include_router(project_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Success Habit AI Studio"
    }