from sqlalchemy import Column, BigInteger, Integer, String, Boolean, TIMESTAMP, ForeignKey, BigInteger
from sqlalchemy.sql import func
from app.db.database import Base


class CMSImage(Base):
    __tablename__ = "cms_images"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    cms_id = Column(BigInteger, ForeignKey("cms.id"), nullable=False)

    file_name = Column(String(255), nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())