from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / '.env')


@dataclass(slots=True)
class Settings:
    database_url: str = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/lab_scalable')
    cors_origins: list[str] = tuple(filter(None, (origin.strip() for origin in os.getenv('BACKEND_CORS_ORIGINS', 'http://127.0.0.1:5173,http://localhost:5173').split(','))))
    seed_on_startup: bool = os.getenv('SEED_ON_STARTUP', 'true').lower() == 'true'
    reset_db_on_startup: bool = os.getenv('RESET_DB_ON_STARTUP', 'false').lower() == 'true'


settings = Settings()
