from sqlalchemy import (
    Column, BigInteger, Integer, String,
    Date, Numeric, Text, TIMESTAMP,
    Enum, ForeignKey
)

from sqlalchemy.sql import func
from app.db.database import Base
from enum import Enum as PyEnum


class ClaimStatus(str, PyEnum):
    Pending = "Pending"
    Approved = "Approved"
    Reject = "Reject"
    ReferBack = "ReferBack"


class Claim(Base):
    __tablename__ = "claim"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    category = Column(String(50), nullable=False)
    mobile = Column(String(255), nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(
        Enum("Pending", "Approved", "Reject", "ReferBack", name="claim_status"),
        nullable=False
    )
    description = Column(Text, nullable=True)
    approval_by = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    manager_comment = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

class ClaimImage(Base):
    __tablename__ = "claim_images"

    id = Column(BigInteger, primary_key=True, index=True)
    claim_id = Column(
        BigInteger,
        ForeignKey("claim.id"),
        nullable=False
    )
    file_upload = Column(String(255), nullable=False)
    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )