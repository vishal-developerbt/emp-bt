from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class ClientMaster(Base):
    __tablename__ = "client_master_list"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    technology = Column(String(255), nullable=True)
    interview_date = Column(String(255), nullable=True)  # ⚠️ keep as string (DB limitation)

    company = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)

    contact_person = Column(String(255), nullable=True)
    client_email = Column(String(255), nullable=True)
    contact_number = Column(String(255), nullable=True)

    source = Column(String(255), nullable=True)
    rate = Column(String(255), nullable=True)

    pre_call_notes = Column(Text, nullable=True)
    meeting_link = Column(Text, nullable=True)
    post_call_notes = Column(Text, nullable=True)

    status = Column(Text, nullable=True)

    interview_taken_by = Column(String(255), nullable=True)
    end_client = Column(String(255), nullable=True)
    interview_type = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())