from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Default to SQLite for local dev; override via DATABASE_URL for Postgres.
    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"


settings = Settings()
