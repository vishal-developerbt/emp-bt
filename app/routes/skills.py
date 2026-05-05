from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.skills import Skill
from app.schemas.skills import SkillCreate, SkillUpdate, SkillResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SkillResponse)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    new_skill = Skill(
        skill_name=skill.skill_name,
        user_id=skill.user_id
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill

@router.put("/{skill_id}", response_model=SkillResponse)
def update_skill(skill_id: int, skill: SkillUpdate, db: Session = Depends(get_db)):
    existing_skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not existing_skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    if skill.skill_name is not None:
        existing_skill.skill_name = skill.skill_name

    if skill.user_id is not None:
        existing_skill.user_id = skill.user_id

    db.commit()
    db.refresh(existing_skill)

    return existing_skill

@router.delete("/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    db.delete(skill)
    db.commit()

    return {"message": "Skill deleted successfully"}