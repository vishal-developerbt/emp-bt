from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpEducation
from app.schemas.employee_schema import (
    EducationCreate,
    EducationUpdate,
    EducationResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EducationResponse)
def create_education(data: EducationCreate, db: Session = Depends(get_db)):
    existing = db.query(EmpEducation).filter(
        EmpEducation.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Education already exists for this user")

    edu = EmpEducation(**data.dict())

    db.add(edu)
    db.commit()
    db.refresh(edu)

    return edu


@router.put("/{id}", response_model=EducationResponse)
def update_education(id: int, data: EducationUpdate, db: Session = Depends(get_db)):
    edu = db.query(EmpEducation).filter(EmpEducation.id == id).first()

    if not edu:
        raise HTTPException(404, "Education not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(edu, field, value)

    db.commit()
    db.refresh(edu)

    return edu


@router.delete("/{id}")
def delete_education(id: int, db: Session = Depends(get_db)):
    edu = db.query(EmpEducation).filter(EmpEducation.id == id).first()

    if not edu:
        raise HTTPException(404, "Education not found")

    db.delete(edu)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[EducationResponse])
def get_all_education(db: Session = Depends(get_db)):
    return db.query(EmpEducation).order_by(EmpEducation.id.desc()).all()

@router.get("/user/{user_id}", response_model=EducationResponse)
def get_user_education(user_id: int, db: Session = Depends(get_db)):
    edu = db.query(EmpEducation).filter(
        EmpEducation.user_id == user_id
    ).first()

    if not edu:
        raise HTTPException(404, "Education not found")

    return edu