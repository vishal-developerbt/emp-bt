from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpShortLeave
from app.schemas.employee_schema import (
    ShortLeaveCreate,
    ShortLeaveUpdate,
    ShortLeaveResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ShortLeaveResponse)
def create_short_leave(data: ShortLeaveCreate, db: Session = Depends(get_db)):
    # Validate dates
    if data.start_date > data.end_date:
        raise HTTPException(400, "Start date cannot be after end date")

    entry = EmpShortLeave(**data.dict())

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry

@router.put("/{id}", response_model=ShortLeaveResponse)
def update_short_leave(id: int, data: ShortLeaveUpdate, db: Session = Depends(get_db)):
    entry = db.query(EmpShortLeave).filter(EmpShortLeave.id == id).first()

    if not entry:
        raise HTTPException(404, "Not found")

    if entry.status != 0:
        raise HTTPException(400, "Cannot edit approved/rejected request")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)

    return entry

@router.delete("/{id}")
def delete_short_leave(id: int, db: Session = Depends(get_db)):
    entry = db.query(EmpShortLeave).filter(EmpShortLeave.id == id).first()

    if not entry:
        raise HTTPException(404, "Not found")

    if entry.status != 0:
        raise HTTPException(400, "Cannot delete approved/rejected request")

    db.delete(entry)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[ShortLeaveResponse])
def get_all_short_leaves(db: Session = Depends(get_db)):
    return db.query(EmpShortLeave).order_by(EmpShortLeave.id.desc()).all()

@router.get("/user/{user_id}", response_model=list[ShortLeaveResponse])
def get_user_short_leaves(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpShortLeave).filter(
        EmpShortLeave.user_id == user_id
    ).all()

@router.put("/approve/{id}")
def approve_short_leave(
    id: int,
    status: int,
    comment: str | None = None,
    db: Session = Depends(get_db)
):
    entry = db.query(EmpShortLeave).filter(EmpShortLeave.id == id).first()

    if not entry:
        raise HTTPException(404, "Not found")

    if status not in [1, 2]:
        raise HTTPException(400, "Invalid status")

    entry.status = status
    entry.comment = comment

    db.commit()

    return {"message": "Updated successfully"}