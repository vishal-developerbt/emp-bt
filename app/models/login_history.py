from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base

class LoginHistory(Base):
    __tablename__ = "login_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    email = Column(String)  # store attempted email
    ip_address = Column(String)
    user_agent = Column(String)

    status = Column(String)  # Success / Failed
    login_time = Column(DateTime, default=datetime.utcnow)