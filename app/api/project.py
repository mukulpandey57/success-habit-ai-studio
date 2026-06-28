from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.project_request import ProjectRequest
from app.schemas.project_response import ProjectResponse
from app.services.project_service import ProjectService

router = APIRouter(tags=["Projects"])

service = ProjectService()


@router.post(
    "/projects",
    response_model=ProjectResponse,
)
def create_project(
    request: ProjectRequest,
    db: Session = Depends(get_db),
):

    project = service.create_project(
        db=db,
        topic=request.topic,
        language=request.language,
        duration=request.duration,
    )

    return ProjectResponse(
        project_id=project.project_id,
        status=project.status,
        project_path=project.project_path,
    )