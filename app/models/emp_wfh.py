from sqlalchemy import Column, BigInteger, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpWFH(Base):
    __tablename__ = "emp_wfhs"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    partical_leave = Column(String(255), nullable=True)  # keep same as DB
    project_manager = Column(String(255), nullable=False)

    approved_by = Column(Integer, nullable=True)
    cc = Column(String(255), nullable=True)

    leave_count = Column(Integer, nullable=False)
    message = Column(Text, nullable=True)

    status = Column(Integer, default=0)  
    # 0 = pending, 1 = approved, 2 = rejected (recommended)

    comment = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())