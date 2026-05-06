from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.emp_salary import EmpSalary
from app.schemas.emp_salary import (
    EmpSalaryCreate,
    EmpSalaryUpdate,
    EmpSalaryResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmpSalaryResponse)
def create_salary(data: EmpSalaryCreate, db: Session = Depends(get_db)):
    # Prevent duplicate (same user + month + year)
    existing = db.query(EmpSalary).filter(
        EmpSalary.user_id == data.user_id,
        EmpSalary.year == data.year,
        EmpSalary.month == data.month
    ).first()

    if existing:
        raise HTTPException(400, "Salary already exists for this month")

    salary = EmpSalary(**data.dict())

    db.add(salary)
    db.commit()
    db.refresh(salary)

    return salary

@router.put("/{id}", response_model=EmpSalaryResponse)
def update_salary(id: int, data: EmpSalaryUpdate, db: Session = Depends(get_db)):
    salary = db.query(EmpSalary).filter(EmpSalary.id == id).first()

    if not salary:
        raise HTTPException(404, "Salary not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(salary, field, value)

    db.commit()
    db.refresh(salary)

    return salary

@router.delete("/{id}")
def delete_salary(id: int, db: Session = Depends(get_db)):
    salary = db.query(EmpSalary).filter(EmpSalary.id == id).first()

    if not salary:
        raise HTTPException(404, "Salary not found")

    db.delete(salary)
    db.commit()

    return {"message": "Deleted successfully"}

@router.get("/", response_model=list[EmpSalaryResponse])
def get_all_salaries(db: Session = Depends(get_db)):
    return db.query(EmpSalary).order_by(
        EmpSalary.year.desc(),
        EmpSalary.month.desc()
    ).all()

@router.get("/user/{user_id}", response_model=list[EmpSalaryResponse])
def get_user_salary(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpSalary).filter(
        EmpSalary.user_id == user_id
    ).order_by(EmpSalary.year.desc()).all()