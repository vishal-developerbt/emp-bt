from sqlalchemy import Column, BigInteger, String, Float, Boolean, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class EmpBand(Base):
    __tablename__ = "emp_band"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    emp_band = Column(String(255), nullable=False)

    basic_salary = Column(Float, default=0.0)
    house_rent_allounce = Column(Float, default=0.0)
    transport_allounce = Column(Float, default=0.0)
    special_allounce = Column(Float, default=0.0)
    extra_pay = Column(Float, default=0.0)

    tds_type = Column(Boolean, default=False)  # True=Yes
    tds = Column(Float, default=0.0)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('emp_band', name='unique_emp_band'),
    )