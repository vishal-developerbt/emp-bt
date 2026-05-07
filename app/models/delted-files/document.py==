from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base
import uuid


class Document(Base):
    __tablename__ = "document"

    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()))

    classification = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)

    document = Column(String(255), nullable=True)  # file path

    name = Column(String(255), nullable=True)

    process_id = Column(String(255), nullable=True)
    profile_id = Column(String(255), nullable=True)
    sub_process_id = Column(String(255), nullable=True)

    tags = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())