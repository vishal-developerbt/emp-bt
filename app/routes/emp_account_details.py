from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.core.utils import validate_ifsc, validate_account
from app.models.emp_account_details import EmpAccountDetails
from app.schemas.emp_account_details import (
    AccountDetailsCreate,
    AccountDetailsUpdate,
    AccountDetailsResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AccountDetailsResponse)
def create_account_details(data: AccountDetailsCreate, db: Session = Depends(get_db)):

    existing = db.query(EmpAccountDetails).filter(
        EmpAccountDetails.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Bank details already exist")

    if data.ifsc and not validate_ifsc(data.ifsc):
        raise HTTPException(400, "Invalid IFSC code")

    if data.acc_no and not validate_account(data.acc_no):
        raise HTTPException(400, "Invalid account number")

    details = EmpAccountDetails(**data.dict())

    db.add(details)
    db.commit()
    db.refresh(details)

    return details

@router.put("/{id}", response_model=AccountDetailsResponse)
def update_account_details(id: int, data: AccountDetailsUpdate, db: Session = Depends(get_db)):
    details = db.query(EmpAccountDetails).filter(EmpAccountDetails.id == id).first()

    if not details:
        raise HTTPException(404, "Record not found")

    if data.ifsc and not validate_ifsc(data.ifsc):
        raise HTTPException(400, "Invalid IFSC code")

    if data.acc_no and not validate_account(data.acc_no):
        raise HTTPException(400, "Invalid account number")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(details, field, value)

    db.commit()
    db.refresh(details)

    return details


@router.get("/user/{user_id}", response_model=AccountDetailsResponse)
def get_user_account_details(user_id: int, db: Session = Depends(get_db)):
    details = db.query(EmpAccountDetails).filter(
        EmpAccountDetails.user_id == user_id
    ).first()

    if not details:
        raise HTTPException(404, "Record not found")

    return details

@router.delete("/{id}")
def delete_account_details(id: int, db: Session = Depends(get_db)):
    details = db.query(EmpAccountDetails).filter(EmpAccountDetails.id == id).first()

    if not details:
        raise HTTPException(404, "Record not found")

    db.delete(details)
    db.commit()

    return {"message": "Deleted successfully"}