from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpPolicy
from app.schemas.employee_schema import (
    EmpPolicyCreate,
    EmpPolicyUpdate,
    EmpPolicyResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmpPolicyResponse)
def create_policy(data: EmpPolicyCreate, db: Session = Depends(get_db)):
    policy = EmpPolicy(**data.dict())

    db.add(policy)
    db.commit()
    db.refresh(policy)

    return policy

@router.put("/{id}", response_model=EmpPolicyResponse)
def update_policy(id: int, data: EmpPolicyUpdate, db: Session = Depends(get_db)):
    policy = db.query(EmpPolicy).filter(EmpPolicy.id == id).first()

    if not policy:
        raise HTTPException(404, "Policy not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(policy, field, value)

    db.commit()
    db.refresh(policy)

    return policy

@router.delete("/{id}")
def delete_policy(id: int, db: Session = Depends(get_db)):
    policy = db.query(EmpPolicy).filter(EmpPolicy.id == id).first()

    if not policy:
        raise HTTPException(404, "Policy not found")

    db.delete(policy)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[EmpPolicyResponse])
def get_all_policies(db: Session = Depends(get_db)):
    return db.query(EmpPolicy).order_by(EmpPolicy.id.desc()).all()