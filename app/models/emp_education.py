from sqlalchemy import Column, BigInteger, Integer, String, TIMESTAMP, UniqueConstraint, ForeignKey, func
from app.db.database import Base


class EmpEducation(Base):
    __tablename__ = "emp_education"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    highschool = Column(String(255), nullable=True)
    intermediate = Column(String(255), nullable=True)
    graduation = Column(String(255), nullable=True)
    post_graduation = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('user_id', name='unique_user_education'),
    )