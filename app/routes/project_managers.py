from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.project_managers import ProjectManager
from app.schemas.project_managers import (
    ProjectManagerCreate,
    ProjectManagerUpdate,
    ProjectManagerResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()\
        
@router.post("/", response_model=ProjectManagerResponse)
def create_project_manager(data: ProjectManagerCreate, db: Session = Depends(get_db)):
    new_entry = ProjectManager(
        project_id=data.project_id,
        manager_id=data.manager_id,
        developer_id=data.developer_id,
        technology_id=data.technology_id,
        status=data.status,
        resource_type=data.resource_type
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@router.put("/{id}", response_model=ProjectManagerResponse)
def update_project_manager(id: int, data: ProjectManagerUpdate, db: Session = Depends(get_db)):
    entry = db.query(ProjectManager).filter(ProjectManager.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)

    return entry

@router.delete("/{id}")
def delete_project_manager(id: int, db: Session = Depends(get_db)):
    entry = db.query(ProjectManager).filter(ProjectManager.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(entry)
    db.commit()

    return {"message": "Deleted successfully"}