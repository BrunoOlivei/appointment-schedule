from functools import lru_cache
from typing import Any, Optional
from pydantic import Field, validator
from pydantic_settings import BaseSettings

from sqlalchemy.engine import URL


class Settings(BaseSettings):
    TITLE: str = "QYON CS-Progress"
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

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_PWS: str = "mauFJcuf5dhRMQrjj"
    MYSQL_USER: str = "example"
    MYSQL_DB: str = "csprogress"

    MYSQL_DATABASE_URI: Optional[URL] = None

    @validator("MYSQL_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str],
                               values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return URL.create(
            "mysql+asyncmy",
            username=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PWS"),
            host=values.get("MYSQL_HOST"),
            port=values.get("MYSQL_PORT"),
            database=values.get("MYSQL_DB"),
        )

    POSTGRESQL_URI: str = ""
    POSTGRESQL_USR: str = ""
    POSTGRESQL_PWD: str = ""
    POSTGRESQL_DB: str = ""

    SQL_SERVER_USR: str = ""
    SQL_SERVER_PWD: str = ""
    SQL_SERVER_HOST: str = ""
    SQL_SERVER_PORT: str = ""
    SQL_SERVER_DB: str = ""

    RABBIT_ENVIRON: str = ""
    RABBIT_EXCHANGE: str = ""
    RABBIT_ROUTING_KEY: str = ""

    URL_HUB: str = ""

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
