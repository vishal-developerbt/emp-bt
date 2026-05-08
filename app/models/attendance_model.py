from sqlalchemy import (
    Column, BigInteger, Integer, String,
    Date, Text, TIMESTAMP, Boolean,
    Enum, UniqueConstraint, ForeignKey
)

from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum as PyEnum


class StatusEnum(str, PyEnum):
    pending = "Pending"
    approved = "Approved"
    reject = "Reject"
    refer_back = "ReferBack"


class Timesheet(Base):
    __tablename__ = "timesheet"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    project_id = Column(BigInteger, ForeignKey("projects.id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    manager_id = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    hours = Column(Integer, nullable=False)
    minutes = Column(Integer, nullable=False)
    select_date = Column(Date, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(
        Enum("pending", "approved", "reject", "refer_back", name="timesheet_status"),
        nullable=False
    )
    manager_comment = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

class TimeSheetComment(Base):
    __tablename__ = "time_sheet_comments"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    timesheet_id = Column(
        BigInteger,
        ForeignKey("timesheet.id"),
        nullable=False
    )
    comment_history = Column(Text, nullable=True)
    status = Column(
        Enum("pending", "approved", "reject", "refer_back", name="timesheet_comment_status"),
        nullable=False
    )
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


class BlockTimesheet(Base):
    __tablename__ = "block_timesheets"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    timesheet_date = Column(Date, nullable=False)
    is_block = Column(Boolean, default=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    approved_by = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    __table_args__ = (
        UniqueConstraint("timesheet_date", "user_id", name="unique_block_per_day_user"),
    )


class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(BigInteger, primary_key=True, index=True)
    holiday_name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    holiday_type = Column(String(50), nullable=False)
    status = Column(Boolean, default=True)
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )