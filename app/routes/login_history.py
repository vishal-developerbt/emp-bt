from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.login_history import LoginHistory
from app.core.deps import get_current_user
from app.db.database import SessionLocal
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_my_login_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(LoginHistory).filter(
        LoginHistory.user_id == current_user.id
    ).order_by(LoginHistory.login_time.desc()).all()