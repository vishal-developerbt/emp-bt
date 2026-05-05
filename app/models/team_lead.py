from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class TeamLead(Base):
    __tablename__ = "team_lead"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    manager_id = Column(Integer, nullable=True)
    teamlead_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)

    status = Column(Integer, default=0)  # 0 = inactive, 1 = active

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())