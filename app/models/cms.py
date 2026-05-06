from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class CMS(Base):
    __tablename__ = "cms"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('title', name='unique_cms_title'),
    )