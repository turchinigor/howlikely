"""Application settings, loaded from environment variables or a .env file."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="HOWLIKELY_", env_file=".env", extra="ignore")

    environment: str = "development"
    data_dir: Path = Path("data/processed")
    duckdb_path: Path = Path("data/processed/howlikely.duckdb")
    cors_origins: list[str] = ["http://localhost:5173"]


settings = Settings()
