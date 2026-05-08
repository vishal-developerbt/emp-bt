from sqlalchemy import Column, BigInteger, Integer, String, Float, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class LoginSession(Base):
    __tablename__ = "login_session"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)

    status = Column(String(255), default="Login")

    work_hours = Column(Float, default=0.0)

    location = Column(String(10), default="WFO")  # WFO / WFH

    comment = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())