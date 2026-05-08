from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.database import SessionLocal
from app.models.employee_model import LoginSession
from app.schemas.employee_schema import SessionCreate, SessionResponse
from app.core.deps import get_current_user
from app.models.employee_model import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=SessionResponse)
def login_session(
    data: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # ❌ prevent multiple active sessions
    active = db.query(LoginSession).filter(
        LoginSession.user_id == current_user.id,
        LoginSession.status == "Login"
    ).first()

    if active:
        raise HTTPException(400, "Already logged in")

    session = LoginSession(
        user_id=current_user.id,
        location=data.location,
        comment=data.comment
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


@router.post("/logout")
def logout_session(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(LoginSession).filter(
        LoginSession.user_id == current_user.id,
        LoginSession.status == "Login"
    ).first()

    if not session:
        raise HTTPException(400, "No active session found")

    # ⏱ Calculate work hours
    now = datetime.utcnow()
    login_time = session.created_at

    hours = (now - login_time).total_seconds() / 3600

    session.status = "Logout"
    session.work_hours = round(hours, 2)

    db.commit()

    return {
        "message": "Logged out successfully",
        "work_hours": session.work_hours
    }


@router.get("/my", response_model=list[SessionResponse])
def my_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(LoginSession).filter(
        LoginSession.user_id == current_user.id
    ).order_by(LoginSession.id.desc()).all()


@router.get("/", response_model=list[SessionResponse])
def all_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    return db.query(LoginSession).order_by(LoginSession.id.desc()).all()