from collections.abc import AsyncGenerator
from typing import Any, Optional

from sqlalchemy.ext.asyncio import (  # type: ignore
    create_async_engine,
    AsyncSession,
    AsyncEngine
)
from sqlalchemy.orm import sessionmaker

from app.core.config import get_config


class Session:
    def __init__(self, driver: str) -> None:
        self.driver = driver
        self._config = get_config()
        self._engine: Optional[AsyncEngine] = self.get_engine()
        self._session = sessionmaker(
            bind=self._engine, class_=AsyncSession, expire_on_commit=False
        )

    def get_engine(self) -> str:
        if self.driver == 'mysql':
            return create_async_engine(
                self._config.MYSQL_DATABASE_URI, echo=True
            )
        elif self.driver == 'postgres':
            return create_async_engine(
                self._config.POSTGRES_DATABASE_URI, echo=True
            )
        else:
            raise Exception("Driver not found")

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, Any]:
        async with self._session() as session:
            yield session
