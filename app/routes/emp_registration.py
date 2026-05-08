from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpRegistration
from app.schemas.employee_schema import (
    EmpRegistrationCreate,
    EmpRegistrationUpdate,
    EmpRegistrationResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmpRegistrationResponse)
def create_employee(data: EmpRegistrationCreate, db: Session = Depends(get_db)):
    # Unique employee code check
    existing = db.query(EmpRegistration).filter(
        EmpRegistration.employee_code == data.employee_code
    ).first()

    if existing:
        raise HTTPException(400, "Employee code already exists")

    emp = EmpRegistration(**data.dict())

    db.add(emp)
    db.commit()
    db.refresh(emp)

    return emp

@router.put("/{id}", response_model=EmpRegistrationResponse)
def update_employee(id: int, data: EmpRegistrationUpdate, db: Session = Depends(get_db)):
    emp = db.query(EmpRegistration).filter(EmpRegistration.id == id).first()

    if not emp:
        raise HTTPException(404, "Employee not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(emp, field, value)

    db.commit()
    db.refresh(emp)

    return emp

@router.delete("/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(EmpRegistration).filter(EmpRegistration.id == id).first()

    if not emp:
        raise HTTPException(404, "Employee not found")

    db.delete(emp)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[EmpRegistrationResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(EmpRegistration).order_by(EmpRegistration.id.desc()).all()