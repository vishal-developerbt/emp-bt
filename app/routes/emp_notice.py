from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpNotice
from app.schemas.employee_schema import (
    NoticeCreate,
    NoticeUpdate,
    NoticeResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NoticeResponse)
def create_notice(data: NoticeCreate, db: Session = Depends(get_db)):
    notice = EmpNotice(**data.dict())

    db.add(notice)
    db.commit()
    db.refresh(notice)

    return notice

@router.put("/{id}", response_model=NoticeResponse)
def update_notice(id: int, data: NoticeUpdate, db: Session = Depends(get_db)):
    notice = db.query(EmpNotice).filter(EmpNotice.id == id).first()

    if not notice:
        raise HTTPException(404, "Notice not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(notice, field, value)

    db.commit()
    db.refresh(notice)

    return notice

@router.delete("/{id}")
def delete_notice(id: int, db: Session = Depends(get_db)):
    notice = db.query(EmpNotice).filter(EmpNotice.id == id).first()

    if not notice:
        raise HTTPException(404, "Notice not found")

    db.delete(notice)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[NoticeResponse])
def get_all_notices(db: Session = Depends(get_db)):
    return db.query(EmpNotice).order_by(EmpNotice.id.desc()).all()