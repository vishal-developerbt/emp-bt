from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class EmpAccountDetails(Base):
    __tablename__ = "emp_account_details"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    bank_name = Column(String(255), nullable=True)
    acc_no = Column(String(50), nullable=True)
    ifsc = Column(String(20), nullable=True)

    salary = Column(String(50), nullable=True)  # keeping as varchar (DB constraint)
    extra_salary = Column(Integer, default=0)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('user_id', name='unique_user_bank_details'),
    )