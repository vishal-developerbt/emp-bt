from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_shift import EmpShift
from app.schemas.emp_shift import (
    EmpShiftCreate,
    EmpShiftUpdate,
    EmpShiftResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmpShiftResponse)
def create_shift(data: EmpShiftCreate, db: Session = Depends(get_db)):
    if data.status not in ["Enable", "Disable"]:
        raise HTTPException(400, "Invalid status")

    shift = EmpShift(**data.dict())

    db.add(shift)
    db.commit()
    db.refresh(shift)

    return shift

@router.put("/{id}", response_model=EmpShiftResponse)
def update_shift(id: int, data: EmpShiftUpdate, db: Session = Depends(get_db)):
    shift = db.query(EmpShift).filter(EmpShift.id == id).first()

    if not shift:
        raise HTTPException(404, "Shift not found")

    if data.status and data.status not in ["Enable", "Disable"]:
        raise HTTPException(400, "Invalid status")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(shift, field, value)

    db.commit()
    db.refresh(shift)

    return shift

@router.delete("/{id}")
def delete_shift(id: int, db: Session = Depends(get_db)):
    shift = db.query(EmpShift).filter(EmpShift.id == id).first()

    if not shift:
        raise HTTPException(404, "Shift not found")

    db.delete(shift)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[EmpShiftResponse])
def get_all_shifts(db: Session = Depends(get_db)):
    return db.query(EmpShift).order_by(EmpShift.id.desc()).all()