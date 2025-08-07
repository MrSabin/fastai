from pathlib import Path
from typing import Annotated

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DeepSeekSettings(BaseSettings):
    API_KEY: SecretStr
    MAX_CONNECTIONS: Annotated[int, Field(gt=0)] = 5


class UnsplashSettings(BaseSettings):
    API_KEY: SecretStr
    MAX_CONNECTIONS: Annotated[int, Field(gt=0)] = 5
    TIMEOUT: Annotated[int, Field(gt=0)] = 20


class Settings(BaseSettings):
    DS: DeepSeekSettings
    US: UnsplashSettings
    USE_MOCKS: bool = False

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )
