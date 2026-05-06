from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.utils import validate_aadhaar, validate_pan
from app.db.database import SessionLocal
from app.models.emp_account import EmpAccount
from app.schemas.emp_account import (
    AccountCreate,
    AccountUpdate,
    AccountResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AccountResponse)
def create_account(data: AccountCreate, db: Session = Depends(get_db)):

    existing = db.query(EmpAccount).filter(
        EmpAccount.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Account already exists")

    if data.addhar_number and not validate_aadhaar(data.addhar_number):
        raise HTTPException(400, "Invalid Aadhaar number")

    if data.pan_number and not validate_pan(data.pan_number):
        raise HTTPException(400, "Invalid PAN number")

    account = EmpAccount(**data.dict())

    db.add(account)
    db.commit()
    db.refresh(account)

    return account

@router.put("/{id}", response_model=AccountResponse)
def update_account(id: int, data: AccountUpdate, db: Session = Depends(get_db)):
    account = db.query(EmpAccount).filter(EmpAccount.id == id).first()

    if not account:
        raise HTTPException(404, "Account not found")

    if data.addhar_number and not validate_aadhaar(data.addhar_number):
        raise HTTPException(400, "Invalid Aadhaar number")

    if data.pan_number and not validate_pan(data.pan_number):
        raise HTTPException(400, "Invalid PAN number")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(account, field, value)

    db.commit()
    db.refresh(account)

    return account


@router.get("/user/{user_id}", response_model=AccountResponse)
def get_user_account(user_id: int, db: Session = Depends(get_db)):
    account = db.query(EmpAccount).filter(
        EmpAccount.user_id == user_id
    ).first()

    if not account:
        raise HTTPException(404, "Account not found")

    return account

@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    account = db.query(EmpAccount).filter(EmpAccount.id == id).first()

    if not account:
        raise HTTPException(404, "Account not found")

    db.delete(account)
    db.commit()

    return {"message": "Deleted successfully"}