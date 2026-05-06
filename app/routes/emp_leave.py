from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.db.database import SessionLocal
from app.models.emp_leave import EmpLeave
from app.schemas.emp_leave import LeaveCreate, LeaveUpdate, LeaveResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=LeaveResponse)
def create_leave(data: LeaveCreate, db: Session = Depends(get_db)):
    # Date validation
    if data.start_date > data.end_date:
        raise HTTPException(400, "Start date cannot be after end date")

    # Overlap check
    overlap = db.query(EmpLeave).filter(
        EmpLeave.user_id == data.user_id,
        EmpLeave.start_date <= data.end_date,
        EmpLeave.end_date >= data.start_date
    ).first()

    if overlap:
        raise HTTPException(400, "Leave already exists in this date range")

    # Leave count validation
    if data.leave_count <= 0:
        raise HTTPException(400, "Invalid leave count")

    leave = EmpLeave(**data.dict())

    db.add(leave)
    db.commit()
    db.refresh(leave)

    return leave

@router.put("/{id}", response_model=LeaveResponse)
def update_leave(id: int, data: LeaveUpdate, db: Session = Depends(get_db)):
    leave = db.query(EmpLeave).filter(EmpLeave.id == id).first()

    if not leave:
        raise HTTPException(404, "Leave not found")

    if leave.status != 0:
        raise HTTPException(400, "Cannot edit approved/rejected leave")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(leave, field, value)

    db.commit()
    db.refresh(leave)

    return leave

@router.get("/", response_model=list[LeaveResponse])
def get_all_leaves(db: Session = Depends(get_db)):
    return db.query(EmpLeave).order_by(EmpLeave.id.desc()).all()


@router.put("/approve/{id}")
def approve_leave(
    id: int,
    status: int,
    comment: str | None = None,
    db: Session = Depends(get_db)
):
    leave = db.query(EmpLeave).filter(EmpLeave.id == id).first()

    if not leave:
        raise HTTPException(404, "Leave not found")

    if status not in [1, 2, 3]:
        raise HTTPException(400, "Invalid status")

    leave.status = status

    db.commit()

    return {"message": "Leave updated successfully"}

@router.get("/user/{user_id}", response_model=list[LeaveResponse])
def get_user_leaves(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpLeave).filter(
        EmpLeave.user_id == user_id
    ).all()