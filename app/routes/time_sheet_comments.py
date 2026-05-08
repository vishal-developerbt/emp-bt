from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.attendance_model import TimeSheetComment
from app.models.attendance_model import Timesheet
from app.schemas.attendance_schema import (
    TimesheetCommentCreate,
    TimesheetCommentUpdate,
    TimesheetCommentResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TimesheetCommentResponse)
def create_comment(data: TimesheetCommentCreate, db: Session = Depends(get_db)):
    # Check timesheet exists
    ts = db.query(Timesheet).filter(Timesheet.id == data.timesheet_id).first()

    if not ts:
        raise HTTPException(404, "Timesheet not found")

    comment = TimesheetComment(
        timesheet_id=data.timesheet_id,
        comment_history=data.comment_history,
        status=data.status
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment

@router.put("/{id}", response_model=TimesheetCommentResponse)
def update_comment(id: int, data: TimesheetCommentUpdate, db: Session = Depends(get_db)):
    comment = db.query(TimesheetComment).filter(TimesheetComment.id == id).first()

    if not comment:
        raise HTTPException(404, "Comment not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(comment, field, value)

    db.commit()
    db.refresh(comment)

    return comment

@router.delete("/{id}")
def delete_comment(id: int, db: Session = Depends(get_db)):
    comment = db.query(TimesheetComment).filter(TimesheetComment.id == id).first()

    if not comment:
        raise HTTPException(404, "Comment not found")

    db.delete(comment)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/timesheet/{timesheet_id}", response_model=list[TimesheetCommentResponse])
def get_comments(timesheet_id: int, db: Session = Depends(get_db)):
    return db.query(TimesheetComment).filter(
        TimesheetComment.timesheet_id == timesheet_id
    ).order_by(TimesheetComment.id.desc()).all()