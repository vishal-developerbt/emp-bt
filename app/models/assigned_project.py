from sqlalchemy import Column, Integer, ForeignKey, Date
from app.db.database import Base

class AssignedProject(Base):
    __tablename__ = "assigned_projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    project_manager_user_id = Column(Integer, ForeignKey("users.id"))
    project_start_date = Column(Date)