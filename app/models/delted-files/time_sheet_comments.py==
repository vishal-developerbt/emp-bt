from sqlalchemy import Column, BigInteger, Integer, Text, String, TIMESTAMP, Enum
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum as PyEnum

class StatusEnum(str, PyEnum):
        pending = "Pending"
        approved = "Approved"
        reject = "Reject"
        refer_back = "ReferBack"

class TimesheetComment(Base):
    __tablename__ = "time_sheet_comments"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    timesheet_id = Column(Integer, nullable=False)
    comment_history = Column(Text, nullable=True)

    #status = Column(String(50), default="Pending")
    status = Column(Enum(StatusEnum), default=StatusEnum.pending, nullable=False)

    #"Pending", "Approved", "Reject", "ReferBack"]
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())


    