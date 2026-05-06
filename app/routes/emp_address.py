from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_address import EmpAddress
from app.schemas.emp_address import (
    AddressCreate,
    AddressUpdate,
    AddressResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AddressResponse)
def create_address(data: AddressCreate, db: Session = Depends(get_db)):

    existing = db.query(EmpAddress).filter(
        EmpAddress.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Address already exists for this user")

    if data.pincode and not data.pincode.isdigit():
        raise HTTPException(400, "Invalid pincode")

    address = EmpAddress(**data.dict())

    db.add(address)
    db.commit()
    db.refresh(address)

    return address

@router.put("/{id}", response_model=AddressResponse)
def update_address(id: int, data: AddressUpdate, db: Session = Depends(get_db)):
    address = db.query(EmpAddress).filter(EmpAddress.id == id).first()

    if not address:
        raise HTTPException(404, "Address not found")

    if data.pincode and not data.pincode.isdigit():
        raise HTTPException(400, "Invalid pincode")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(address, field, value)

    db.commit()
    db.refresh(address)

    return address


@router.delete("/{id}")
def delete_address(id: int, db: Session = Depends(get_db)):
    address = db.query(EmpAddress).filter(EmpAddress.id == id).first()

    if not address:
        raise HTTPException(404, "Address not found")

    db.delete(address)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/", response_model=list[AddressResponse])
def get_all_addresses(db: Session = Depends(get_db)):
    return db.query(EmpAddress).order_by(EmpAddress.id.desc()).all()

@router.get("/user/{user_id}", response_model=AddressResponse)
def get_user_address(user_id: int, db: Session = Depends(get_db)):
    address = db.query(EmpAddress).filter(
        EmpAddress.user_id == user_id
    ).first()

    if not address:
        raise HTTPException(404, "Address not found")

    return address