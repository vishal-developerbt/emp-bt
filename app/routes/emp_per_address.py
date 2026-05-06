from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_per_address import EmpPerAddress
from app.schemas.emp_per_address import (
    PerAddressCreate,
    PerAddressUpdate,
    PerAddressResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PerAddressResponse)
def create_address(data: PerAddressCreate, db: Session = Depends(get_db)):
    # Prevent duplicate per user
    existing = db.query(EmpPerAddress).filter(
        EmpPerAddress.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Address already exists for this user")

    # Pincode validation (India example)
    if data.p_pincode and not data.p_pincode.isdigit():
        raise HTTPException(400, "Invalid pincode")

    address = EmpPerAddress(**data.dict())

    db.add(address)
    db.commit()
    db.refresh(address)

    return address


@router.put("/{id}", response_model=PerAddressResponse)
def update_address(id: int, data: PerAddressUpdate, db: Session = Depends(get_db)):
    address = db.query(EmpPerAddress).filter(EmpPerAddress.id == id).first()

    if not address:
        raise HTTPException(404, "Address not found")

    if data.p_pincode and not data.p_pincode.isdigit():
        raise HTTPException(400, "Invalid pincode")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(address, field, value)

    db.commit()
    db.refresh(address)

    return address

@router.delete("/{id}")
def delete_address(id: int, db: Session = Depends(get_db)):
    address = db.query(EmpPerAddress).filter(EmpPerAddress.id == id).first()

    if not address:
        raise HTTPException(404, "Address not found")

    db.delete(address)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[PerAddressResponse])
def get_all_addresses(db: Session = Depends(get_db)):
    return db.query(EmpPerAddress).order_by(EmpPerAddress.id.desc()).all()

@router.get("/user/{user_id}", response_model=PerAddressResponse)
def get_user_address(user_id: int, db: Session = Depends(get_db)):
    address = db.query(EmpPerAddress).filter(
        EmpPerAddress.user_id == user_id
    ).first()

    if not address:
        raise HTTPException(404, "Address not found")

    return address