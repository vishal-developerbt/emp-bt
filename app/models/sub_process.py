from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.mysql import JSON
from app.db.database import Base
from datetime import datetime


class SubProcess(Base):
    __tablename__ = "sub_process"

    id = Column(String(255), primary_key=True, index=True)

    created_by = Column(String(255), nullable=True)
    creation_date = Column(DateTime, default=datetime.utcnow)

    last_modified_by = Column(String(255), nullable=True)
    last_modified_date = Column(DateTime, onupdate=datetime.utcnow)

    client_cell = Column(String(255), nullable=True)
    client_email = Column(String(255), nullable=True)

    interview_date = Column(String(255), nullable=False)
    interview_mode = Column(String(255), nullable=True)
    interview_panel = Column(String(255), nullable=True)

    meeting_invite = Column(Text, nullable=True)
    note = Column(Text, nullable=True)

    properties = Column(JSON, nullable=True)

    status = Column(String(255), nullable=True)
    time = Column(String(255), nullable=True)

    consultant_id = Column(String(255), ForeignKey("profile.id"), nullable=True)
    process_id = Column(String(255), ForeignKey("process.id"), nullable=True)

    profile = Column(String(255), nullable=True)