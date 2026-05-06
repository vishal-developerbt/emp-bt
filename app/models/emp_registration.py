from sqlalchemy import Column, BigInteger, Integer, String, Date, Float, Boolean, TIMESTAMP,Enum
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum as PyEnum

class EmployeeBand(str, PyEnum):
    E1 = "E1"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E5 = "E5"

class EmpRegistration(Base):
    __tablename__ = "emp_registrations"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)
    employee_code = Column(String(255), nullable=False)

    dob = Column(Date, nullable=False)
    gender = Column(String(50), nullable=False)

    job_title = Column(String(255), nullable=False)
    employment_type = Column(String(255), nullable=True)

    blood_group = Column(String(50), nullable=True)

    special_leave = Column(Float, default=0)
    casual_leave = Column(Float, default=0)
    sick_leave = Column(Float, default=0)

    employee_band = Column(Enum(EmployeeBand, name="employee_band_enum"), default=EmployeeBand.E1)
    joining_date = Column(Date, nullable=False)
    relieving_date = Column(Date, nullable=True)

    accept_policy = Column(String(20), default="Pending")

    status = Column(Boolean, default=True)  # ✅ fixed

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())