from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base

class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    basic = Column(Float)
    hra = Column(Float)
    bonus = Column(Float)
    deductions = Column(Float)

    month = Column(String)  # e.g. "April 2026"