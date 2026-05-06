from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.department import Department
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse
)
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DepartmentResponse)
def create_department(
    data: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    existing = db.query(Department).filter(
        Department.department_name == data.department_name
    ).first()

    if existing:
        raise HTTPException(400, "Department already exists")

    dept = Department(**data.dict())

    db.add(dept)
    db.commit()
    db.refresh(dept)

    return dept

@router.post("/", response_model=DepartmentResponse)
def create_department(
    data: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    existing = db.query(Department).filter(
        Department.department_name == data.department_name
    ).first()

    if existing:
        raise HTTPException(400, "Department already exists")

    dept = Department(**data.dict())

    db.add(dept)
    db.commit()
    db.refresh(dept)

    return dept


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).order_by(Department.id.desc()).all()

@router.get("/active", response_model=list[DepartmentResponse])
def get_active_departments(db: Session = Depends(get_db)):
    return db.query(Department).filter(
        Department.status == True
    ).all()

@router.delete("/{id}")
def delete_department(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    dept = db.query(Department).filter(Department.id == id).first()

    if not dept:
        raise HTTPException(404, "Department not found")

    db.delete(dept)
    db.commit()

    return {"message": "Deleted successfully"}