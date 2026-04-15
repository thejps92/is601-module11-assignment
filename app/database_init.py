from app.database import Base, get_engine


def init_db() -> None:
    # Ensure models are imported so SQLAlchemy registers them on Base.metadata
    import app.models.user  # noqa: F401
    import app.models.calculation  # noqa: F401

    engine = get_engine()
    Base.metadata.create_all(bind=engine)


def drop_db() -> None:
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":  # pragma: no cover
    init_db()
