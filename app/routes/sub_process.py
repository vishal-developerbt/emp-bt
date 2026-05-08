from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import uuid

from app.db.database import SessionLocal
from app.models.project_model import SubProcess
from app.models.project_model import Process
from app.models.employee_model import Profile

from app.schemas.project_schema import (
    SubProcessCreate,
    SubProcessUpdate,
    SubProcessResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SubProcessResponse)
def create_sub_process(data: SubProcessCreate, db: Session = Depends(get_db)):

    # ✅ Validate process
    if data.process_id:
        process = db.query(Process).filter(Process.id == data.process_id).first()
        if not process:
            raise HTTPException(404, "Process not found")

    # ✅ Validate consultant
    if data.consultant_id:
        consultant = db.query(Profile).filter(Profile.id == data.consultant_id).first()
        if not consultant:
            raise HTTPException(404, "Consultant not found")

    sub = SubProcess(
        id=str(uuid.uuid4()),
        **data.dict()
    )

    db.add(sub)
    db.commit()
    db.refresh(sub)

    return sub


@router.get("/", response_model=list[SubProcessResponse])
def get_sub_processes(
    process_id: str | None = Query(None),
    status: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(SubProcess)

    if process_id:
        query = query.filter(SubProcess.process_id == process_id)

    if status:
        query = query.filter(SubProcess.status.ilike(f"%{status}%"))

    return query.order_by(SubProcess.creation_date.desc()).all()


@router.get("/{id}", response_model=SubProcessResponse)
def get_sub_process(id: str, db: Session = Depends(get_db)):

    sub = db.query(SubProcess).filter(SubProcess.id == id).first()

    if not sub:
        raise HTTPException(404, "Sub process not found")

    return sub


@router.put("/{id}", response_model=SubProcessResponse)
def update_sub_process(id: str, data: SubProcessUpdate, db: Session = Depends(get_db)):

    sub = db.query(SubProcess).filter(SubProcess.id == id).first()

    if not sub:
        raise HTTPException(404, "Sub process not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(sub, field, value)

    db.commit()
    db.refresh(sub)

    return sub


@router.delete("/{id}")
def delete_sub_process(id: str, db: Session = Depends(get_db)):

    sub = db.query(SubProcess).filter(SubProcess.id == id).first()

    if not sub:
        raise HTTPException(404, "Sub process not found")

    db.delete(sub)
    db.commit()

    return {"message": "Deleted successfully"}