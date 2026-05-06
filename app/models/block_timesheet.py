from sqlalchemy import Column, BigInteger, Integer, Date, Boolean, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


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