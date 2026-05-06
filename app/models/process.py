from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import JSON
from app.db.database import Base
from datetime import datetime


class Process(Base):
    __tablename__ = "process"

    id = Column(String(255), primary_key=True, index=True)

    created_by = Column(String(255), nullable=True)
    creation_date = Column(DateTime, default=datetime.utcnow)

    last_modified_by = Column(String(255), nullable=True)
    last_modified_date = Column(DateTime, onupdate=datetime.utcnow)

    client = Column(String(255), nullable=True)
    client_cell = Column(String(255), nullable=True)
    client_email = Column(String(255), nullable=True)
    client_poc = Column(String(255), nullable=True)

    data_source = Column(String(255), nullable=True)

    properties = Column(JSON, nullable=True)

    rate = Column(String(255), nullable=True)
    source = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)

    candidate_id = Column(String(255), ForeignKey("profile.id"), nullable=True)

    consultant = Column(String(255), nullable=True)
    contact_id = Column(String(255), nullable=True)

    tags = Column(String(255), default="NOT TAGGED")