from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_feedback import EmpFeedback
from app.schemas.emp_feedback import (
    FeedbackCreate,
    FeedbackUpdate,
    FeedbackResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FeedbackResponse)
def create_feedback(data: FeedbackCreate, db: Session = Depends(get_db)):
    if data.user_id == data.reviewer_id:
        raise HTTPException(400, "User cannot review themselves")

    feedback = EmpFeedback(**data.dict())

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return feedback

@router.put("/{id}", response_model=FeedbackResponse)
def update_feedback(id: int, data: FeedbackUpdate, db: Session = Depends(get_db)):
    feedback = db.query(EmpFeedback).filter(EmpFeedback.id == id).first()

    if not feedback:
        raise HTTPException(404, "Feedback not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(feedback, field, value)

    db.commit()
    db.refresh(feedback)

    return feedback

@router.delete("/{id}")
def delete_feedback(id: int, db: Session = Depends(get_db)):
    feedback = db.query(EmpFeedback).filter(EmpFeedback.id == id).first()

    if not feedback:
        raise HTTPException(404, "Feedback not found")

    db.delete(feedback)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[FeedbackResponse])
def get_all_feedbacks(db: Session = Depends(get_db)):
    return db.query(EmpFeedback).order_by(EmpFeedback.id.desc()).all()

@router.get("/user/{user_id}", response_model=list[FeedbackResponse])
def get_user_feedback(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpFeedback).filter(
        EmpFeedback.user_id == user_id
    ).all()


@router.get("/reviewer/{reviewer_id}", response_model=list[FeedbackResponse])
def get_reviewer_feedback(reviewer_id: int, db: Session = Depends(get_db)):
    return db.query(EmpFeedback).filter(
        EmpFeedback.reviewer_id == reviewer_id
    ).all()