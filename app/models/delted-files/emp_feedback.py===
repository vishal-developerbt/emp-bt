from sqlalchemy import Column, BigInteger, Integer, Boolean, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.database import Base


class EmpFeedback(Base):
    __tablename__ = "emp_feedbacks"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, nullable=False)       # receiver
    reviewer_id = Column(Integer, nullable=False)   # reviewer

    status = Column(Boolean, default=True)

    message = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())