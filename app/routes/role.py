from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import Role
from app.schemas.employee_schema import RoleCreate, RoleUpdate, RoleResponse
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    new_role = Role(
        department=role.department,
        access=role.access,
        status=role.status
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role

@router.put("/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    existing_role = db.query(Role).filter(Role.id == role_id).first()

    if not existing_role:
        raise HTTPException(status_code=404, detail="Role not found")

    if role.department is not None:
        existing_role.department = role.department

    if role.access is not None:
        existing_role.access = role.access

    if role.status is not None:
        existing_role.status = role.status

    db.commit()
    db.refresh(existing_role)

    return existing_role