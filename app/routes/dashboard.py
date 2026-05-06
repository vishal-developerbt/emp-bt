from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.db.database import SessionLocal
from app.models.user import User
from app.models.timesheet import Timesheet
from app.models.emp_leave import EmpLeave
from app.core.deps import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = date.today()

    # Total Hours (current user)
    total_hours = db.query(Timesheet).filter(
        Timesheet.user_id == current_user.id
    ).with_entities(Timesheet.hours).all()

    total_hours_sum = sum([h[0] for h in total_hours]) if total_hours else 0

    # 🌴 Total Leaves
    total_leaves = db.query(EmpLeave).filter(
        EmpLeave.user_id == current_user.id
    ).count()

    # Upcoming Birthdays (next 7 days)
    upcoming_birthdays = []
    users = db.query(User).all()

    for user in users:
        if user.dob:
            next_birthday = user.dob.replace(year=today.year)

            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)

            if 0 <= (next_birthday - today).days <= 7:
                upcoming_birthdays.append({
                    "name": user.name,
                    "date": next_birthday
                })

    # Work Anniversary (next 7 days)
    upcoming_anniversaries = []

    for user in users:
        if user.joining_date:
            next_anniversary = user.joining_date.replace(year=today.year)

            if next_anniversary < today:
                next_anniversary = next_anniversary.replace(year=today.year + 1)

            if 0 <= (next_anniversary - today).days <= 7:
                upcoming_anniversaries.append({
                    "name": user.name,
                    "date": next_anniversary
                })

    # 🌴 Today Employees on Leave
    today_leaves = db.query(EmpLeave).filter(
        EmpLeave.start_date <= today,
        EmpLeave.end_date >= today,
        EmpLeave.status == "Approved"
    ).all()

    today_leave_users = []
    for leave in today_leaves:
        user = db.query(User).filter(User.id == leave.user_id).first()
        if user:
            today_leave_users.append({
                "name": user.name,
                "email": user.email
            })

    return {
        "total_hours": total_hours_sum,
        "total_leaves": total_leaves,
        "upcoming_birthdays": upcoming_birthdays,
        "upcoming_anniversaries": upcoming_anniversaries,
        "today_on_leave": today_leave_users
    }