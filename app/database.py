from __future__ import annotations

from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings


Base = declarative_base()


@lru_cache
def get_engine(database_url: str | None = None):
    url = database_url or settings.DATABASE_URL
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=connect_args)


def get_sessionmaker(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    engine = get_engine()
    SessionLocal = get_sessionmaker(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
