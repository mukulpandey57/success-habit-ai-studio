from pydantic import BaseModel


class StoryRequest(BaseModel):
    topic: str
    language: str = "Hindi"
    duration: int = 40
    audience: str = "Kids"