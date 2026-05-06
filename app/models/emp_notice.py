from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpNotice(Base):
    __tablename__ = "emp_notice"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    color = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())