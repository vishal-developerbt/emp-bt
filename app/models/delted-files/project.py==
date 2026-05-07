from sqlalchemy import Column, BigInteger, String, Date, Boolean, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    project_name = Column(String(255), nullable=False)
    vendor_name = Column(String(255), nullable=False)

    project_startdate = Column(Date, nullable=False)
    project_enddate = Column(Date, nullable=True)

    status = Column(Boolean, default=True)   # enum(0,1) → Boolean

    is_billable = Column(SmallInteger, default=1)  # 1 = billable, 0 = non-billable

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())