from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.database import Base


class Technology(Base):
    __tablename__ = "technology"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    technology = Column(String(100), nullable=True)
    status = Column(Boolean, default=True)  # 1 = active, 0 = inactive

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())