from sqlalchemy import Column, BigInteger, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class Manager(Base):
    __tablename__ = "managers"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    manager_name = Column(String(255), nullable=False)
    skill_type = Column(String(255), nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())