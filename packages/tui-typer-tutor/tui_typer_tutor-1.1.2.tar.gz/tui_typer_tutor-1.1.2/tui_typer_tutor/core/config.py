"""Config."""

from functools import lru_cache
from pathlib import Path

from beartype import beartype
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_SEED_FILE = Path(__file__).parent / 'seed_data.txt'
"""Default seed file if not specified."""


class Config(BaseSettings):
    """Application config."""

    seed_file: Path = DEFAULT_SEED_FILE
    model_config = SettingsConfigDict(env_prefix='TYPER_')


@lru_cache(maxsize=1)
@beartype
def get_config() -> Config:
    """Retrieve the application config."""
    return Config()
