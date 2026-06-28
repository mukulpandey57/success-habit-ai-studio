from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.db import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(String, unique=True, nullable=False, index=True)

    title = Column(String, nullable=True)

    topic = Column(String, nullable=False)

    language = Column(String, default="Hindi")

    duration = Column(Integer, default=30)

    status = Column(String, default="CREATED")

    project_path = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )