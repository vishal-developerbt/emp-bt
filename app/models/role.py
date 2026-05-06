from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    department = Column(String(255), nullable=False)
    access = Column(Text, nullable=True)  # JSON or string
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now()) 