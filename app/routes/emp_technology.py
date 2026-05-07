from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpTechnology
from app.schemas.employee_schema import (
    EmpTechnologyCreate,
    EmpTechnologyUpdate,
    EmpTechnologyResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EmpTechnologyResponse)
def create_technology(data: EmpTechnologyCreate, db: Session = Depends(get_db)):
    tech = EmpTechnology(**data.dict())

    db.add(tech)
    db.commit()
    db.refresh(tech)

    return tech

@router.put("/{id}", response_model=EmpTechnologyResponse)
def update_technology(id: int, data: EmpTechnologyUpdate, db: Session = Depends(get_db)):
    tech = db.query(EmpTechnology).filter(EmpTechnology.id == id).first()

    if not tech:
        raise HTTPException(404, "Technology not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(tech, field, value)

    db.commit()
    db.refresh(tech)

    return tech

@router.delete("/{id}")
def delete_technology(id: int, db: Session = Depends(get_db)):
    tech = db.query(EmpTechnology).filter(EmpTechnology.id == id).first()

    if not tech:
        raise HTTPException(404, "Technology not found")

    db.delete(tech)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[EmpTechnologyResponse])
def get_all_technology(db: Session = Depends(get_db)):
    return db.query(EmpTechnology).order_by(EmpTechnology.id.desc()).all()