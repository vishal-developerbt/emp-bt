from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import TeamLead
from app.schemas.project_schema import (
    TeamLeadCreate,
    TeamLeadUpdate,
    TeamLeadResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TeamLeadResponse)
def create_team_lead(data: TeamLeadCreate, db: Session = Depends(get_db)):
    new_entry = TeamLead(
        manager_id=data.manager_id,
        teamlead_id=data.teamlead_id,
        user_id=data.user_id,
        status=data.status
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@router.put("/{id}", response_model=TeamLeadResponse)
def update_team_lead(id: int, data: TeamLeadUpdate, db: Session = Depends(get_db)):
    entry = db.query(TeamLead).filter(TeamLead.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")

    if data.manager_id is not None:
        entry.manager_id = data.manager_id

    if data.teamlead_id is not None:
        entry.teamlead_id = data.teamlead_id

    if data.user_id is not None:
        entry.user_id = data.user_id

    if data.status is not None:
        entry.status = data.status

    db.commit()
    db.refresh(entry)

    return entry

@router.delete("/{id}")
def delete_team_lead(id: int, db: Session = Depends(get_db)):
    entry = db.query(TeamLead).filter(TeamLead.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(entry)
    db.commit()

    return {"message": "Deleted successfully"}