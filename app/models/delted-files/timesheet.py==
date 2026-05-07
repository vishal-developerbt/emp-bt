from sqlalchemy import Column, BigInteger, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class Timesheet(Base):
    __tablename__ = "timesheet"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    project_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    manager_id = Column(Integer, nullable=True)

    hours = Column(String(255), nullable=False)
    minutes = Column(String(255), nullable=False)

    select_date = Column(Date, nullable=False)
    description = Column(Text, nullable=True)

    status = Column(String(50), default="Pending")  
    # Pending, Approved, Reject, ReferBack

    manager_comment = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())