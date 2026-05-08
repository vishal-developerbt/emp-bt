from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee_model import EmpSkill
from app.schemas.employee_schema import (
    EmpSkillCreate,
    EmpSkillUpdate,
    EmpSkillResponse
)

router = APIRouter(prefix="/emp-skill", tags=["Emp Skill"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmpSkillResponse)
def create_emp_skill(data: EmpSkillCreate, db: Session = Depends(get_db)):
    # Prevent duplicate (same user + skill)
    existing = db.query(EmpSkill).filter(
        EmpSkill.user_id == data.user_id,
        EmpSkill.skill_id == data.skill_id
    ).first()

    if existing:
        raise HTTPException(400, "Skill already assigned to user")

    # Validate skill level
    if data.skill_level not in ["Beginner", "Proficient", "Expert"]:
        raise HTTPException(400, "Invalid skill level")

    skill = EmpSkill(**data.dict())

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill

@router.put("/{id}", response_model=EmpSkillResponse)
def update_emp_skill(id: int, data: EmpSkillUpdate, db: Session = Depends(get_db)):
    skill = db.query(EmpSkill).filter(EmpSkill.id == id).first()

    if not skill:
        raise HTTPException(404, "Skill not found")

    if data.skill_level:
        if data.skill_level not in ["Beginner", "Proficient", "Expert"]:
            raise HTTPException(400, "Invalid skill level")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(skill, field, value)

    db.commit()
    db.refresh(skill)

    return skill

@router.delete("/{id}")
def delete_emp_skill(id: int, db: Session = Depends(get_db)):
    skill = db.query(EmpSkill).filter(EmpSkill.id == id).first()

    if not skill:
        raise HTTPException(404, "Skill not found")

    db.delete(skill)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/", response_model=list[EmpSkillResponse])
def get_all_emp_skills(db: Session = Depends(get_db)):
    return db.query(EmpSkill).order_by(EmpSkill.id.desc()).all()

@router.get("/user/{user_id}", response_model=list[EmpSkillResponse])
def get_user_skills(user_id: int, db: Session = Depends(get_db)):
    return db.query(EmpSkill).filter(
        EmpSkill.user_id == user_id,
        EmpSkill.status == True
    ).all()