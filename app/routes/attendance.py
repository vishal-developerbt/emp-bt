from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date, timezone
from app.db.database import SessionLocal
from app.models.attendance import Attendance
from app.models.user import User
from app.core.deps import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Check-In
@router.post("/check-in")
def check_in(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = date.today()

    existing = db.query(Attendance).filter(
        Attendance.user_id == current_user.id,
        Attendance.date == today
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already checked in today")

    attendance = Attendance(
        user_id=current_user.id,
        date=today,
        check_in = datetime.now(timezone.utc)
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return {"message": "Checked in successfully", "time": attendance.check_in}


# Check-Out
@router.post("/check-out")
def check_out(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = date.today()

    attendance = db.query(Attendance).filter(
        Attendance.user_id == current_user.id,
        Attendance.date == today
    ).first()

    if not attendance:
        raise HTTPException(status_code=400, detail="Check-in first")

    if attendance.check_out:
        raise HTTPException(status_code=400, detail="Already checked out")

    attendance.check_out = datetime.now(timezone.utc)

    db.commit()

    return {"message": "Checked out successfully", "time": attendance.check_out}


# Get My Attendance
@router.get("/")
def get_attendance(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    records = db.query(Attendance).filter(
        Attendance.user_id == current_user.id
    ).all()

    return records
