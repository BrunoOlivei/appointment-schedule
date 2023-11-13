from functools import lru_cache
from typing import Any, Optional
from pydantic import Field, validator
from pydantic_settings import BaseSettings

from sqlalchemy.engine import URL


class Settings(BaseSettings):
    TITLE: str = "DIB Scheduler"
    VERSION: str = "1.0"
    TIMEZONE: str = "utc-3"
    DESCRIPTION: str | None = None
    DEBUG: bool = False

    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    API_PREFIX_V1: str = "/api/v1"

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # CORS_ORIGINS is a string of ';' separated origins.
    # e.g:  'http://localhost:8080;http://localhost:3000'
    # CORS_ORIGINS: list[AnyHttpUrl]

    POSTGRESQL_URI: str
    POSTGRESQL_USR: str
    POSTGRESQL_PWD: str
    POSTGRESQL_PORT: int = 5432
    POSTGRESQL_DB: str

    POSTGRESQL_DATABASE_URI: Optional[URL] = None

    @validator("POSTGRESQL_DATABASE_URI", pre=True)
    def assemble_postgresql_connection(
        cls,
        v: Optional[str],
        values: dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return URL.create(
            "postgresql+asyncpg",
            username=values.get("POSTGRESQL_PANEL_USR"),
            password=values.get("POSTGRESQL_PANEL_PWD"),
            host=values.get("POSTGRESQL_PANEL_URI"),
            port=values.get("POSTGRESQL_PANEL_PORT"),
            database=values.get("POSTGRESQL_PANEL_DB"),
        )

    RABBIT_ENVIRON: str = ""
    RABBIT_EXCHANGE: str = ""
    RABBIT_ROUTING_KEY: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True

        # @classmethod
        # def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
        #     if field_name == "CORS_ORIGINS":
        #         return [origin for origin in raw_val.split(";")]
        #     # The following line is ignored by mypy because:
        #     # error: Type'[Config]' has no attribute 'json_loads',
        #     # even though it is like the documentation:
        #     # https://docs.pydantic.dev/latest/usage/settings/
        #     return cls.json_loads(raw_val)  # type: ignore[attr-defined]


@lru_cache()
def get_config() -> Settings:
    return Settings()  # type: ignore[call-arg]
