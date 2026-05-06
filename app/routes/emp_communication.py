from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_communication import EmpCommunication
from app.schemas.emp_communication import (
    CommunicationCreate,
    CommunicationUpdate,
    CommunicationResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CommunicationResponse)
def create_communication(data: CommunicationCreate, db: Session = Depends(get_db)):

    existing = db.query(EmpCommunication).filter(
        EmpCommunication.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Communication already exists for this user")

    if data.mobile_number and not data.mobile_number.isdigit():
        raise HTTPException(400, "Invalid mobile number")

    comm = EmpCommunication(**data.dict())

    db.add(comm)
    db.commit()
    db.refresh(comm)

    return comm

@router.put("/{id}", response_model=CommunicationResponse)
def update_communication(id: int, data: CommunicationUpdate, db: Session = Depends(get_db)):
    comm = db.query(EmpCommunication).filter(EmpCommunication.id == id).first()

    if not comm:
        raise HTTPException(404, "Record not found")

    if data.mobile_number and not data.mobile_number.isdigit():
        raise HTTPException(400, "Invalid mobile number")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(comm, field, value)

    db.commit()
    db.refresh(comm)

    return comm

@router.delete("/{id}")
def delete_communication(id: int, db: Session = Depends(get_db)):
    comm = db.query(EmpCommunication).filter(EmpCommunication.id == id).first()

    if not comm:
        raise HTTPException(404, "Record not found")

    db.delete(comm)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/", response_model=list[CommunicationResponse])
def get_all_communication(db: Session = Depends(get_db)):
    return db.query(EmpCommunication).order_by(EmpCommunication.id.desc()).all()


@router.get("/user/{user_id}", response_model=CommunicationResponse)
def get_user_communication(user_id: int, db: Session = Depends(get_db)):
    comm = db.query(EmpCommunication).filter(
        EmpCommunication.user_id == user_id
    ).first()

    if not comm:
        raise HTTPException(404, "Record not found")

    return comm