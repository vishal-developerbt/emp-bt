from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.timesheet import Timesheet
from app.schemas.timesheet import (
    TimesheetCreate,
    TimesheetUpdate,
    TimesheetResponse,
    TimesheetStatusUpdate
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TimesheetResponse)
def create_timesheet(data: TimesheetCreate, db: Session = Depends(get_db)):
    new_entry = Timesheet(**data.dict())

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@router.put("/{id}", response_model=TimesheetResponse)
def update_timesheet(id: int, data: TimesheetUpdate, db: Session = Depends(get_db)):
    entry = db.query(Timesheet).filter(Timesheet.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Timesheet not found")

    if entry.status != "Pending":
        raise HTTPException(status_code=400, detail="Only pending timesheets can be updated")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)

    return entry


@router.put("/{id}/status", response_model=TimesheetResponse)
def update_timesheet_status(id: int, data: TimesheetStatusUpdate, db: Session = Depends(get_db)):
    entry = db.query(Timesheet).filter(Timesheet.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Timesheet not found")

    entry.status = data.status
    entry.manager_comment = data.manager_comment

    db.commit()
    db.refresh(entry)

    return entry

@router.delete("/{id}")
def delete_timesheet(id: int, db: Session = Depends(get_db)):
    entry = db.query(Timesheet).filter(Timesheet.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Timesheet not found")

    db.delete(entry)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[TimesheetResponse])
def get_all_timesheets(db: Session = Depends(get_db)):
    return db.query(Timesheet).order_by(Timesheet.select_date.desc()).all()