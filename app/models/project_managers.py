from sqlalchemy import Column, BigInteger, Integer, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class ProjectManager(Base):
    __tablename__ = "project_managers"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    project_id = Column(Integer, nullable=False)
    manager_id = Column(Integer, nullable=False)
    developer_id = Column(Integer, nullable=False)
    technology_id = Column(Integer, nullable=False)

    status = Column(Boolean, default=True)       # ✅ replaced ENUM
    resource_type = Column(Boolean, default=False)  # 0/1 → False/True

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())