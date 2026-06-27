from fastapi import FastAPI

from app.api.health import router as health_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.include_router(health_router)


@app.get("/")
def root():

    return {
        "message": "Welcome to Success Habit AI Studio"
    }