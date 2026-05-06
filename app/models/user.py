from sqlalchemy import (
    Column, BigInteger, String, Integer, TIMESTAMP
)
from sqlalchemy.sql import func
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    name = Column(String(255), nullable=False)

    employee_code = Column(String(255), unique=True, nullable=False)
    role = Column(String(255), nullable=False, default="employee")

    email = Column(String(255), unique=True, nullable=False, index=True)
    email_verified_at = Column(TIMESTAMP, nullable=True)

    password = Column(String(255), nullable=False)

    remember_token = Column(String(100), nullable=True)
    reset_password_token = Column(String(100), nullable=True)
    token_status = Column(String(10), nullable=True)

    emp_shift_id = Column(Integer, default=1)
    technology_id = Column(Integer, nullable=True)

    timesheet_skip = Column(Integer, default=0)  # 0 = No, 1 = Yes
    is_paid = Column(Integer, default=1)         # 1 = Paid, 0 = Unpaid

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())