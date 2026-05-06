from sqlalchemy import Column, BigInteger, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpPolicy(Base):
    __tablename__ = "emp_policy"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    hr_policy_leave_mang = Column(String(255), nullable=True)
    hr_process_onboarding = Column(String(255), nullable=True)
    hr_process_offboarding = Column(String(255), nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())