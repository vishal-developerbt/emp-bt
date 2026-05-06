from sqlalchemy import Column, BigInteger, Integer, Date, Text, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpIncrement(Base):
    __tablename__ = "emp_increment"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    increment_date = Column(Date, nullable=True)
    next_increment_date = Column(Date, nullable=True)

    increment_amount = Column(Integer, nullable=True)

    old_salary = Column(Integer, nullable=True)
    new_salary = Column(Integer, nullable=True)

    comment = Column(Text, nullable=True)

    is_increment_done = Column(Boolean, default=False)

    increment_interval = Column(Integer, nullable=False)  # months

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())