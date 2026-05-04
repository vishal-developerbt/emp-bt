from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)      # Travel / Food / etc
    amount = Column(Float)
    description = Column(String)

    status = Column(String, default="Pending")  # Pending / Approved / Rejected