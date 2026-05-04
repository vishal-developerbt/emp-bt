from sqlalchemy import Column, DateTime, Integer, String, Date
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="employee")
    username = Column(String, unique=True, index=True)

     # Profile fields
    dob = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    blood_group = Column(String, nullable=True)
    joining_date = Column(Date, nullable=True)
    employee_type = Column(String, nullable=True)
    employee_band = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    shift = Column(String, nullable=True)
    reset_otp = Column(String, nullable=True)
    otp_expiry = Column(DateTime, nullable=True)