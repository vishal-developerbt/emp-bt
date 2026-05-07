from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpPrevEmployment
from app.schemas.employee_schema import (
    PrevEmploymentCreate,
    PrevEmploymentUpdate,
    PrevEmploymentResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PrevEmploymentResponse)
def create_prev_employment(data: PrevEmploymentCreate, db: Session = Depends(get_db)):
    entry = EmpPrevEmployment(**data.dict())

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry

@router.put("/{id}", response_model=PrevEmploymentResponse)
def update_prev_employment(id: int, data: PrevEmploymentUpdate, db: Session = Depends(get_db)):
    entry = db.query(EmpPrevEmployment).filter(EmpPrevEmployment.id == id).first()

    if not entry:
        raise HTTPException(404, "Record not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)

    return entry

@router.delete("/{id}")
def delete_prev_employment(id: int, db: Session = Depends(get_db)):
    entry = db.query(EmpPrevEmployment).filter(EmpPrevEmployment.id == id).first()

    if not entry:
        raise HTTPException(404, "Record not found")

    db.delete(entry)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/", response_model=list[PrevEmploymentResponse])
def get_all_prev_employment(db: Session = Depends(get_db)):
    return db.query(EmpPrevEmployment).order_by(EmpPrevEmployment.id.desc()).all()

@router.get("/user/{user_id}", response_model=list[PrevEmploymentResponse])
def get_user_prev_employment(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpPrevEmployment).filter(
        EmpPrevEmployment.user_id == user_id
    ).all()