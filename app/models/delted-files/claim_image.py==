from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base


class ClaimImage(Base):
    __tablename__ = "claim_images"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    claim_id = Column(BigInteger, ForeignKey("claim.id"), nullable=False)

    file_upload = Column(String(255), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())