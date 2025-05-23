from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB = "sqlite:///./mytest.db"

engine = create_engine(
    SQL_DB, connect_args={"check_same_thread": False}

)
SessioLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_connection():
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()