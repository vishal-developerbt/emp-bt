from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_family_details import EmpFamilyDetails
from app.schemas.emp_family_details import (
    FamilyCreate,
    FamilyUpdate,
    FamilyResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FamilyResponse)
def create_family(data: FamilyCreate, db: Session = Depends(get_db)):

    if data.contact_number and not data.contact_number.isdigit():
        raise HTTPException(400, "Invalid contact number")

    if data.number_type and data.number_type not in [1, 2, 3, 4]:
        raise HTTPException(400, "Invalid number type")

    entry = EmpFamilyDetails(**data.dict())

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry

@router.put("/{id}", response_model=FamilyResponse)
def update_family(id: int, data: FamilyUpdate, db: Session = Depends(get_db)):
    entry = db.query(EmpFamilyDetails).filter(EmpFamilyDetails.id == id).first()

    if not entry:
        raise HTTPException(404, "Record not found")

    if data.contact_number and not data.contact_number.isdigit():
        raise HTTPException(400, "Invalid contact number")

    if data.number_type and data.number_type not in [1, 2, 3, 4]:
        raise HTTPException(400, "Invalid number type")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)

    return entry

@router.delete("/{id}")
def delete_family(id: int, db: Session = Depends(get_db)):
    entry = db.query(EmpFamilyDetails).filter(EmpFamilyDetails.id == id).first()

    if not entry:
        raise HTTPException(404, "Record not found")

    db.delete(entry)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/user/{user_id}", response_model=list[FamilyResponse])
def get_user_family(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpFamilyDetails).filter(
        EmpFamilyDetails.user_id == user_id
    ).all()
