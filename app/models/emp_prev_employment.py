from sqlalchemy import Column, BigInteger, Integer, Text, TIMESTAMP, DATE, VARCHAR
from sqlalchemy.sql import func
from app.db.database import Base


class EmpPrevEmployment(Base):
    __tablename__ = "emp_prev_employments"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    start_date = Column(DATE, nullable=True)
    end_date = Column(DATE, nullable=True)

    company_name = Column(VARCHAR(255), nullable=True)
    role = Column(Text, nullable=True)

    company_emp_ref_name = Column(Text, nullable=True)
    company_emp_ref_email = Column(Text, nullable=True)
    company_emp_ref_mobile = Column(Text, nullable=True)
    company_emp_ref_role = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())