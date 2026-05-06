from sqlalchemy import Column, BigInteger, Integer, Float, String, Boolean, TIMESTAMP, Enum
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum as PyEnum

class SkillLevel(str, PyEnum):
    beginner = "Beginner"
    proficient = "Proficient"
    expert = "Expert"

class EmpSkill(Base):
    __tablename__ = "emp_skill"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    skill_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    skill_level = Column(Enum(SkillLevel, name="skill_level_enum"))  # Beginner, Proficient, Expert
    experience = Column(Float, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())