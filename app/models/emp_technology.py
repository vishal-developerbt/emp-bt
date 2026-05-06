from sqlalchemy import Column, BigInteger, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpTechnology(Base):
    __tablename__ = "emp_technology"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    tech_name = Column(String(255), nullable=True)
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())