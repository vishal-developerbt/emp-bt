from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import uuid

from app.db.database import SessionLocal
from app.models.project_model import Process
from app.schemas.project_schema import (
    ProcessCreate,
    ProcessUpdate,
    ProcessResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProcessResponse)
def create_process(data: ProcessCreate, db: Session = Depends(get_db)):

    process = Process(
        id=str(uuid.uuid4()),
        **data.dict()
    )

    db.add(process)
    db.commit()
    db.refresh(process)

    return process


@router.get("/", response_model=list[ProcessResponse])
def get_processes(
    status: str | None = Query(None),
    client: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Process)

    if status:
        query = query.filter(Process.status.ilike(f"%{status}%"))

    if client:
        query = query.filter(Process.client.ilike(f"%{client}%"))

    return query.order_by(Process.creation_date.desc()).all()

@router.get("/{id}", response_model=ProcessResponse)
def get_process(id: str, db: Session = Depends(get_db)):

    process = db.query(Process).filter(Process.id == id).first()

    if not process:
        raise HTTPException(404, "Process not found")

    return process


@router.put("/{id}", response_model=ProcessResponse)
def update_process(id: str, data: ProcessUpdate, db: Session = Depends(get_db)):

    process = db.query(Process).filter(Process.id == id).first()

    if not process:
        raise HTTPException(404, "Process not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(process, field, value)

    db.commit()
    db.refresh(process)

    return process


@router.delete("/{id}")
def delete_process(id: str, db: Session = Depends(get_db)):

    process = db.query(Process).filter(Process.id == id).first()

    if not process:
        raise HTTPException(404, "Process not found")

    db.delete(process)
    db.commit()

    return {"message": "Deleted successfully"}