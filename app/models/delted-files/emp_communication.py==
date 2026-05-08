from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class EmpCommunication(Base):
    __tablename__ = "emp_communications"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    mobile_number = Column(String(20), nullable=True)
    company_email_id = Column(String(255), nullable=True)
    internal_email_id = Column(String(255), nullable=True)
    email_id = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('user_id', name='unique_user_communication'),
    )