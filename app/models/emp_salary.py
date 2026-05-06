from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, Float, Boolean
from sqlalchemy.sql import func
from app.db.database import Base


class EmpSalary(Base):
    __tablename__ = "emp_salary"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)
    credit_salary = Column(Float)

    year = Column(Integer, nullable=False)
    month = Column(Integer)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())