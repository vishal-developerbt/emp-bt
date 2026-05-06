from sqlalchemy import Column, BigInteger, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpPerAddress(Base):
    __tablename__ = "emp_per_address"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    p_house_no = Column(String(255), nullable=False)
    p_street = Column(Text, nullable=True)
    p_city = Column(String(255), nullable=True)
    p_state = Column(String(255), nullable=True)
    p_country = Column(String(255), nullable=True)
    p_pincode = Column(String(20), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())