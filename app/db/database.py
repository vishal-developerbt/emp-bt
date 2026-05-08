from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://smartbank_user:smartbank123@localhost:5432/mybluethink"
#DATABASE_URL = "mysql+pymysql://magento2:magento123@localhost:3306/mybluethink?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    echo=True  # optional
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()