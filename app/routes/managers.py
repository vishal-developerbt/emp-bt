from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.managers import Manager
from app.schemas.managers import (
    ManagerCreate,
    ManagerUpdate,
    ManagerResponse
)

router = APIRouter(prefix="/managers", tags=["Managers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ManagerResponse)
def create_manager(data: ManagerCreate, db: Session = Depends(get_db)):
    new_manager = Manager(
        manager_name=data.manager_name,
        skill_type=data.skill_type,
        status=data.status
    )

    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    return new_manager

@router.put("/{id}", response_model=ManagerResponse)
def update_manager(id: int, data: ManagerUpdate, db: Session = Depends(get_db)):
    manager = db.query(Manager).filter(Manager.id == id).first()

    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    if data.manager_name is not None:
        manager.manager_name = data.manager_name

    if data.skill_type is not None:
        manager.skill_type = data.skill_type

    if data.status is not None:
        manager.status = data.status

    db.commit()
    db.refresh(manager)

    return manager

@router.delete("/{id}")
def delete_manager(id: int, db: Session = Depends(get_db)):
    manager = db.query(Manager).filter(Manager.id == id).first()

    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    db.delete(manager)
    db.commit()

    return {"message": "Manager deleted successfully"}