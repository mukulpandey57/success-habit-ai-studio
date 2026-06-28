from pydantic import BaseModel


class ProjectRequest(BaseModel):
    topic: str
    language: str = "Hindi"
    duration: int = 40