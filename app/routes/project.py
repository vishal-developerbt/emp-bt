from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date

from app.db.database import SessionLocal
from app.models.project_model import Project
from app.schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)
from app.core.deps import get_current_user
from app.models.employee_model import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProjectResponse)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    # Validation
    if data.project_enddate and data.project_startdate > data.project_enddate:
        raise HTTPException(400, "End date must be after start date")

    existing = db.query(Project).filter(
        Project.project_name == data.project_name
    ).first()

    if existing:
        raise HTTPException(400, "Project already exists")

    project = Project(**data.dict())

    db.add(project)
    db.commit()
    db.refresh(project)

    return project

@router.put("/{id}", response_model=ProjectResponse)
def update_project(
    id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(404, "Project not found")

    # Date validation
    if data.project_startdate and data.project_enddate:
        if data.project_startdate > data.project_enddate:
            raise HTTPException(400, "Invalid date range")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(project, field, value)

    db.commit()
    db.refresh(project)

    return project


@router.get("/", response_model=list[ProjectResponse])
def get_projects(
    status: bool | None = Query(None),
    is_billable: int | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Project)

    if status is not None:
        query = query.filter(Project.status == status)

    if is_billable is not None:
        query = query.filter(Project.is_billable == is_billable)

    return query.order_by(Project.id.desc()).all()

@router.get("/{id}", response_model=ProjectResponse)
def get_project(id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(404, "Project not found")

    return project


@router.delete("/{id}")
def delete_project(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(404, "Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Deleted successfully"}