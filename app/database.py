import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv("VERCEL"):
    DEFAULT_DB_PATH = Path("/tmp") / "todos.db"
else:
    DEFAULT_DB_PATH = BASE_DIR / "todos.db"

if os.getenv("DATABASE_URL"):
    db_url = os.getenv("DATABASE_URL")
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
    DATABASE_URL = db_url
else:
    if os.getenv("VERCEL"):
        DATABASE_URL = f"sqlite:////{DEFAULT_DB_PATH}"
    else:
        DATABASE_URL = f"sqlite:///{DEFAULT_DB_PATH}"

connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
