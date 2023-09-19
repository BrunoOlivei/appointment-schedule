from collections.abc import AsyncGenerator
from typing import Any, Optional

from sqlalchemy.ext.asyncio import (  # type: ignore
    create_async_engine,
    AsyncSession,
    AsyncEngine
)
from sqlalchemy.orm import sessionmaker

from app.core.config import get_config


config = get_config()
engine: AsyncEngine = create_async_engine(config.MYSQL_DATABASE_URI, echo=True)
Session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    async with Session() as session:
        yield session


class Session:
    def __init__(self, driver: str) -> None:
        self.driver = driver
        self._config = get_config()
        self._engine: Optional[AsyncEngine] = self.get_uri()
        self._session = sessionmaker(
            bind=engine, class_=AsyncSession, expire_on_commit=False
        )

    def get_uri(self) -> str:
        if self.driver == 'mysql':
            return create_async_engine(
                config.MYSQL_DATABASE_URI, echo=True
            )
        elif self.driver == 'postgres':
            return create_async_engine(
                config.POSTGRES_DATABASE_URI, echo=True
            )
        else:
            raise Exception("Driver not found")

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, Any]:
        async with self._session() as session:
            yield session
