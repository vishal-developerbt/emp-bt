from sqlalchemy import Column, BigInteger, String, TIMESTAMP, Boolean
from sqlalchemy.sql import func
from app.db.database import Base


class EmpShift(Base):
    __tablename__ = "emp_shift"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    shift_name = Column(String(255), nullable=True)
    timezone = Column(String(255), nullable=True)
    shift_start_time = Column(String(50), nullable=False)
    logged_in_by = Column(String(50), nullable=False)

    status = Column(Boolean, default=True)  # Enable / Disable

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())