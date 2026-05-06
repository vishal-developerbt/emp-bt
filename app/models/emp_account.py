from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class EmpAccount(Base):
    __tablename__ = "emp_accounts"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    profile_pic = Column(String(255), nullable=True)

    addhar_number = Column(String(20), nullable=True)
    addhar_doc_file = Column(String(255), nullable=True)

    pan_number = Column(String(20), nullable=True)
    pan_doc_file = Column(String(255), nullable=True)

    offer_letter = Column(String(255), nullable=True)
    relieving_latter = Column(String(255), nullable=True)
    resignation_letter = Column(String(255), nullable=True)
    appointment_latter = Column(String(255), nullable=True)

    bank_statment = Column(String(255), nullable=True)

    salary_slip1 = Column(String(255), nullable=True)
    salary_slip2 = Column(String(255), nullable=True)
    salary_slip3 = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('user_id', name='unique_user_account'),
    )