from sqlalchemy import Column, BigInteger, Integer, String, Date, Float, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class Claim(Base):
    __tablename__ = "claim"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    category = Column(String(50), nullable=False)

    mobile = Column(String(255), nullable=True)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    amount = Column(Float, nullable=False)

    status = Column(String(20), default="Pending")

    description = Column(Text, nullable=True)

    approval_by = Column(Integer, default=0)
    manager_comment = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())