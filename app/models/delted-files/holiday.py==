from sqlalchemy import Column, BigInteger, String, Date, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    holiday_name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)

    # Instead of ENUM('Company Holiday','Restricted Holiday')
    type = Column(String(50), nullable=False)

    # ENUM('0','1') → Boolean
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())