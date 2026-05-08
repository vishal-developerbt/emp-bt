from sqlalchemy import Column, BigInteger, Integer, String, Date, Text, TIMESTAMP, Boolean, Enum, UniqueConstraint, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum as PyEnum

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


class BlockTimesheet(Base):
    __tablename__ = "block_timesheets"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    timesheet_date = Column(Date, nullable=False)

    is_block = Column(Boolean, default=True)

    user_id = Column(Integer, default=0)  # 0 = global block

    approved_by = Column(Integer, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('timesheet_date', 'user_id', name='unique_block_per_day_user'),
    )


class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    holiday_name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)

    # Instead of ENUM('Company Holiday','Restricted Holiday')
    type = Column(String(50), nullable=False)

    # ENUM('0','1') → Boolean
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())