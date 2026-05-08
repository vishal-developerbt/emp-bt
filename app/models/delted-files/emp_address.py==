from sqlalchemy import Column, BigInteger, Integer, String, Text, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class EmpAddress(Base):
    __tablename__ = "emp_addresses"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    house_no = Column(String(255), nullable=True)
    street = Column(Text, nullable=True)
    city = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    pincode = Column(String(20), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('user_id', name='unique_user_current_address'),
    )