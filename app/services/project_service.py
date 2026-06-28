import os
from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from app.database.models import Project


class ProjectService:

    def create_project(
        self,
        db: Session,
        topic: str,
        language: str,
        duration: int,
    ):

        project_id = (
            f"prj_{datetime.now().strftime('%Y%m%d_%H%M%S')}_"
            f"{uuid4().hex[:6]}"
        )

        project_path = os.path.join("projects", project_id)

        folders = [
            "story",
            "scenes",
            "images",
            "audio",
            "subtitles",
            "video",
            "thumbnail",
            "metadata",
            "logs",
        ]

        for folder in folders:
            os.makedirs(
                os.path.join(project_path, folder),
                exist_ok=True,
            )

        project = Project(
            project_id=project_id,
            topic=topic,
            language=language,
            duration=duration,
            status="CREATED",
            project_path=project_path,
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return project