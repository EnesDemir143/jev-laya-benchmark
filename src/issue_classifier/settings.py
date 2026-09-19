from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """Load TypeSafe config from the environment / `.env`. Never log the key."""

    model_config = SettingsConfigDict(
        env_file=_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    typesafe_api_key: SecretStr
    typesafe_base_url: str | None = None
    typesafe_default_model: str = "jev-latest"
    noul_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    typesafe_timeout: float = Field(default=30.0, gt=0.0)
