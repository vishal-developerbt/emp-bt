from sqlalchemy import Column, BigInteger, Integer, String, Date, Float, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpLeave(Base):
    __tablename__ = "emp_leaves"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    partical_leave = Column(String(255), nullable=True)
    leave_type = Column(String(255), nullable=False)

    project_manager = Column(String(255), nullable=False)
    approved_by = Column(Integer, nullable=True)
    applied_by = Column(Integer, nullable=False)

    cc = Column(String(255), nullable=True)

    leave_count = Column(Float, nullable=False)
    message = Column(Text, nullable=True)

    status = Column(Integer, default=0)  # 0=pending

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())