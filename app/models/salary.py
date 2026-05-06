from sqlalchemy import Column, Integer, String, Float, ForeignKey, BigInteger
from app.db.database import Base

class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))

    basic = Column(Float)
    hra = Column(Float)
    bonus = Column(Float)
    deductions = Column(Float)

    month = Column(String(20))   # e.g. "April 2026"