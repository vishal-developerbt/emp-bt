from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.project_model import SkillDepartment
from app.schemas.project_schema import (
    SkillDepartmentCreate,
    SkillDepartmentUpdate,
    SkillDepartmentResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SkillDepartmentResponse)
def create_skill_department(
    skill: SkillDepartmentCreate,
    db: Session = Depends(get_db)
):
    new_skill = SkillDepartment(
        skill_name=skill.skill_name,
        status=skill.status
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill

@router.put("/{skill_id}", response_model=SkillDepartmentResponse)
def update_skill_department(
    skill_id: int,
    skill: SkillDepartmentUpdate,
    db: Session = Depends(get_db)
):
    existing_skill = db.query(SkillDepartment).filter(
        SkillDepartment.id == skill_id
    ).first()

    if not existing_skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    if skill.skill_name is not None:
        existing_skill.skill_name = skill.skill_name

    if skill.status is not None:
        existing_skill.status = skill.status

    db.commit()
    db.refresh(existing_skill)

    return existing_skill