# Load .env
from env import Settings
config = Settings()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import HTTPException, status

if not config.IS_DEBUG:
    SQLALCHEMY_DATABASE_URL = "sqlite:////app/data/sql_app.db"
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./data/sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()