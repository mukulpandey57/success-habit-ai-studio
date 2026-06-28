from fastapi import APIRouter

from app.schemas.story_request import StoryRequest
from app.services.ollama_service import OllamaService

router = APIRouter(tags=["Story"])

ollama = OllamaService()


@router.post("/generate-story")
def generate_story(request: StoryRequest):

    prompt = f"""
Write a {request.duration} second {request.language} motivational story for {request.audience}.

Topic:
{request.topic}

Story Rules:
- Grandfather teaches grandson.
- Moral at the end.
- Easy Hindi.
"""

    story = ollama.generate(prompt)

    return {
        "topic": request.topic,
        "story": story
    }