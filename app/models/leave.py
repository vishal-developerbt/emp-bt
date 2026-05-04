from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    start_date = Column(Date)
    end_date = Column(Date)
    reason = Column(String)

    status = Column(String, default="Pending")  # Pending / Approved / Rejected

    user = relationship("User")