from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "ok",
        "service": "Success Habit AI Studio"
    }