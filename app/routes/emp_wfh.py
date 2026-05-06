from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_wfh import EmpWFH
from app.schemas.emp_wfh import (
    EmpWFHCreate,
    EmpWFHUpdate,
    EmpWFHResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EmpWFHResponse)
def create_wfh(data: EmpWFHCreate, db: Session = Depends(get_db)):
    new_entry = EmpWFH(**data.dict())

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@router.put("/{id}", response_model=EmpWFHResponse)
def update_wfh(id: int, data: EmpWFHUpdate, db: Session = Depends(get_db)):
    entry = db.query(EmpWFH).filter(EmpWFH.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="WFH not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(entry, field, value)

    db.commit()
    db.refresh(entry)

    return entry

@router.get("/", response_model=list[EmpWFHResponse])
def get_all_wfh(db: Session = Depends(get_db)):
    return db.query(EmpWFH).order_by(EmpWFH.id.desc()).all()