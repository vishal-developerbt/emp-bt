from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.leave import Leave
from app.schemas.leave import LeaveCreate, LeaveResponse
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Apply Leave
@router.post("/", response_model=LeaveResponse)
def apply_leave(
    data: LeaveCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if data.end_date < data.start_date:
        raise HTTPException(status_code=400, detail="End date cannot be before start date")

    leave = Leave(
        user_id=current_user.id,
        start_date=data.start_date,
        end_date=data.end_date,
        reason=data.reason
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)

    return leave


# Get My Leaves
@router.get("/", response_model=list[LeaveResponse])
def get_my_leaves(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Leave).filter(
        Leave.user_id == current_user.id
    ).all()


# Admin Approve / Reject
@router.put("/approve/{id}")
def approve_leave(
    id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    leave = db.query(Leave).filter(Leave.id == id).first()

    if not leave:
        raise HTTPException(status_code=404, detail="Not found")

    if status not in ["Approved", "Rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    leave.status = status
    db.commit()

    return {"message": f"Leave {status}"}