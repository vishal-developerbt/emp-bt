from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpFamilyDetails(Base):
    __tablename__ = "emp_family_details"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    father_name = Column(String(255), nullable=True)
    mother_name = Column(String(255), nullable=True)
    spouse_name = Column(String(255), nullable=True)

    number_type = Column(Integer, nullable=True)  # 1=Father,2=Mother,3=Spouse,4=Emergency
    contact_number = Column(String(20), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())