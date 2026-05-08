from sqlalchemy import Column, BigInteger, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class SkillDepartment(Base):
    __tablename__ = "skill_department"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    skill_name = Column(String(255), nullable=False)

    # since DB uses enum('0','1')
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())