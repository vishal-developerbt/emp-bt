from sqlalchemy import (
    Column, BigInteger, String, Text,
    Boolean, TIMESTAMP, UniqueConstraint,
    ForeignKey, text
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base


class CMS(Base):
    __tablename__ = "cms"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    images = relationship("CMSImage", backref="cms", cascade="all, delete")

    __table_args__ = (
        UniqueConstraint('title', name='unique_cms_title'),
    )


class CMSImage(Base):
    __tablename__ = "cms_images"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    cms_id = Column(BigInteger, ForeignKey("cms.id"), nullable=False)

    file_name = Column(String(255), nullable=False)

    status = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())


class EmailTemplate(Base):
    __tablename__ = "email_templates"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    subject = Column(String(255), nullable=False)

    type = Column(String(255), nullable=False)

    content = Column(Text, nullable=False)

    status = Column(Boolean, nullable=False, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('type', name='unique_email_type'),
    )


class CityState(Base):
    __tablename__ = "city_states"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint('state', 'city', name='unique_state_city'),
    )