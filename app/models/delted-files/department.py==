from sqlalchemy import Column, BigInteger, String, Boolean, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class Department(Base):
    __tablename__ = "department"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    department_name = Column(String(255), nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('department_name', name='unique_department_name'),
    )