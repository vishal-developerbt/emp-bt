from sqlalchemy import Column, BigInteger, String, UniqueConstraint
from app.db.database import Base


class CityState(Base):
    __tablename__ = "city_states"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint('state', 'city', name='unique_state_city'),
    )