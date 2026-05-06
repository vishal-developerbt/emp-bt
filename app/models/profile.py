from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import JSON
from app.db.database import Base
from datetime import datetime


class Profile(Base):
    __tablename__ = "profile"

    id = Column(String(255), primary_key=True, index=True)

    created_by = Column(String(255), nullable=True)
    creation_date = Column(DateTime, default=datetime.utcnow)

    last_modified_by = Column(String(255), nullable=True)
    last_modified_date = Column(DateTime, onupdate=datetime.utcnow)

    email = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    mobile = Column(String(255), nullable=True)

    properties = Column(JSON, nullable=True)

    type = Column(String(255), nullable=True)
    code = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)