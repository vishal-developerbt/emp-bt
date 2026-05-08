from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class EmailTemplate(Base):
    __tablename__ = "email_templates"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    subject = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)  # unique key
    content = Column(Text, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('type', name='unique_email_type'),
    )