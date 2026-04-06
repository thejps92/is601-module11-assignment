from __future__ import annotations

from sqlalchemy import inspect

from app.config import settings
from app.database import get_engine
from app.database_init import drop_db, init_db


def test_init_db_creates_users_table_and_drop_db_removes_it(tmp_path):
    get_engine.cache_clear()

    db_file = tmp_path / "init.db"
    settings.DATABASE_URL = f"sqlite:///{db_file}"

    init_db()

    engine = get_engine()
    inspector = inspect(engine)
    assert "users" in inspector.get_table_names()

    drop_db()

    inspector = inspect(engine)
    assert "users" not in inspector.get_table_names()
