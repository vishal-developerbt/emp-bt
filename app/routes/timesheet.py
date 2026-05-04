from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date
from app.db.database import SessionLocal
from app.models.timesheet import Timesheet
from app.models.assigned_project import AssignedProject
from app.schemas.timesheet import TimesheetCreate, TimesheetResponse
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Timesheet
@router.post("/", response_model=TimesheetResponse)
def create_timesheet(
    data: TimesheetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check project assignment
    assignment = db.query(AssignedProject).filter(
        AssignedProject.user_id == current_user.id,
        AssignedProject.project_id == data.project_id
    ).first()

    if not assignment:
        raise HTTPException(status_code=403, detail="Project not assigned")

    # Prevent duplicate (same date + project)
    existing = db.query(Timesheet).filter(
        Timesheet.user_id == current_user.id,
        Timesheet.project_id == data.project_id,
        Timesheet.date == data.date
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Timesheet already exists for this date & project"
        )

    # Max hours validation
    if data.hours > 8:
        raise HTTPException(status_code=400, detail="Max 8 hours allowed")

    ts = Timesheet(
        user_id=current_user.id,
        project_id=data.project_id,
        date=data.date,
        hours=data.hours,
        description=data.description
    )

    db.add(ts)
    db.commit()
    db.refresh(ts)

    return ts


# Update Timesheet
@router.put("/{id}", response_model=TimesheetResponse)
def update_timesheet(
    id: int,
    data: TimesheetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ts = db.query(Timesheet).filter(
        Timesheet.id == id,
        Timesheet.user_id == current_user.id
    ).first()

    if not ts:
        raise HTTPException(status_code=404, detail="Not found")

    if ts.status != "Pending":
        raise HTTPException(
            status_code=400,
            detail="Cannot edit approved/rejected timesheet"
        )

    # Validate project assignment again
    assignment = db.query(AssignedProject).filter(
        AssignedProject.user_id == current_user.id,
        AssignedProject.project_id == data.project_id
    ).first()

    if not assignment:
        raise HTTPException(status_code=403, detail="Project not assigned")

    ts.project_id = data.project_id
    ts.date = data.date
    ts.hours = data.hours
    ts.description = data.description

    db.commit()
    db.refresh(ts)

    return ts


# Get My Timesheets (with filters)
@router.get("/", response_model=list[TimesheetResponse])
def get_timesheets(
    from_date: date | None = Query(None),
    to_date: date | None = Query(None),
    status: str | None = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Timesheet).filter(
        Timesheet.user_id == current_user.id
    )

    if from_date:
        query = query.filter(Timesheet.date >= from_date)

    if to_date:
        query = query.filter(Timesheet.date <= to_date)

    if status:
        query = query.filter(Timesheet.status == status)

    return query.order_by(Timesheet.date.desc()).all()


# Delete Timesheet
@router.delete("/{id}")
def delete_timesheet(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ts = db.query(Timesheet).filter(
        Timesheet.id == id,
        Timesheet.user_id == current_user.id
    ).first()

    if not ts:
        raise HTTPException(status_code=404, detail="Not found")

    if ts.status != "Pending":
        raise HTTPException(
            status_code=400,
            detail="Cannot delete approved/rejected timesheet"
        )

    db.delete(ts)
    db.commit()

    return {"message": "Deleted successfully"}


# Approve / Reject (Admin Only)
@router.put("/approve/{id}")
def approve_timesheet(
    id: int,
    status: str = Query(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    ts = db.query(Timesheet).filter(Timesheet.id == id).first()

    if not ts:
        raise HTTPException(status_code=404, detail="Not found")

    if status not in ["Approved", "Rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    ts.status = status
    db.commit()

    return {"message": f"Timesheet {status}"}