from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://postgres:password@localhost:5432/mybluethink"
DATABASE_URL = "postgresql://smartbank_user:smartbank123@localhost:5432/mybluethink"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()