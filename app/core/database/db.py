from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy.ext.asyncio import (  # type: ignore
    create_async_engine,
    AsyncSession,
    AsyncEngine
)
from sqlalchemy.orm import sessionmaker

from app.core.settings.config import get_config

class AsyncSessionMaker:
    def __init__(self) -> None:
        self.__config = get_config()

    def get_engine(self) -> AsyncEngine:
        
        try:
            return create_async_engine(
                self.__config.POSTGRES_DATABASE_URI, echo=True
                )
        except Exception as e:
            raise e

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, Any]:
        engine = self.get_engine()
        session = sessionmaker(
            bind=engine, class_=AsyncSession, expire_on_commit=False
        )
        async with session() as session:
            yield session
