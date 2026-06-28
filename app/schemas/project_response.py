from pydantic import BaseModel


class ProjectResponse(BaseModel):
    project_id: str
    status: str
    project_path: str