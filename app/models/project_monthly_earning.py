from sqlalchemy import Column, Integer, Float, Date, DateTime, ForeignKey, UniqueConstraint, BigInteger
from sqlalchemy.sql import func
from app.db.database import Base


class ProjectMonthlyEarning(Base):
    __tablename__ = "project_monthly_earning"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    project_id = Column(BigInteger, ForeignKey("projects.id"), nullable=False)

    month = Column(Date, nullable=False)  # store as YYYY-MM-01

    earning = Column(Float, nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('project_id', 'month', name='unique_project_month'),
    )