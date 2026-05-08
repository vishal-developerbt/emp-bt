from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.utils import calculate_next_increment
from app.db.database import SessionLocal
from app.models.employee_model import EmpIncrement
from app.schemas.employee_schema import (
    IncrementCreate,
    IncrementUpdate,
    IncrementResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=IncrementResponse)
def create_increment(data: IncrementCreate, db: Session = Depends(get_db)):

    if data.old_salary and data.new_salary:
        if data.new_salary < data.old_salary:
            raise HTTPException(400, "New salary must be greater than old salary")

    next_date = None
    if data.increment_date:
        next_date = calculate_next_increment(data.increment_date, data.increment_interval)

    increment = EmpIncrement(
        **data.dict(),
        next_increment_date=next_date
    )

    db.add(increment)
    db.commit()
    db.refresh(increment)

    return increment


@router.put("/{id}", response_model=IncrementResponse)
def update_increment(id: int, data: IncrementUpdate, db: Session = Depends(get_db)):
    inc = db.query(EmpIncrement).filter(EmpIncrement.id == id).first()

    if not inc:
        raise HTTPException(404, "Increment not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(inc, field, value)

    # recalc next increment if needed
    if inc.increment_date and inc.increment_interval:
        inc.next_increment_date = calculate_next_increment(
            inc.increment_date,
            inc.increment_interval
        )

    db.commit()
    db.refresh(inc)

    return inc

@router.delete("/{id}")
def delete_increment(id: int, db: Session = Depends(get_db)):
    inc = db.query(EmpIncrement).filter(EmpIncrement.id == id).first()

    if not inc:
        raise HTTPException(404, "Increment not found")

    db.delete(inc)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/", response_model=list[IncrementResponse])
def get_all_increments(db: Session = Depends(get_db)):
    return db.query(EmpIncrement).order_by(EmpIncrement.id.desc()).all()

@router.get("/user/{user_id}", response_model=list[IncrementResponse])
def get_user_increments(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpIncrement).filter(
        EmpIncrement.user_id == user_id
    ).all()

@router.put("/mark-done/{id}")
def mark_increment_done(id: int, db: Session = Depends(get_db)):
    inc = db.query(EmpIncrement).filter(EmpIncrement.id == id).first()

    if not inc:
        raise HTTPException(404, "Increment not found")

    inc.is_increment_done = True
    db.commit()

    return {"message": "Increment marked as done"}