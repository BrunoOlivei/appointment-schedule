from typing import Optional
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from app.core.actions.base import ActionsBase
from app.core.actions.constants import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT
)

from app.users.models.permissions import PermissionUser
from app.users.schemas.permission_user import (
    PermissionUserInDB,
)


class PermissionUserActions:
    def __init__(self) -> None:
        self._repo = ActionsBase()

    async def get_permissions(
        self,
        session: AsyncSession,
        *,
        skip: int = GET_MULTI_DEFAULT_SKIP,
        limit: int = GET_MULTI_DEFAULT_LIMIT
    ) -> list[PermissionUser]:
        return await self._repo.get_multi(
            session,
            table_model=PermissionUser,
            skip=skip,
            limit=limit,
        )
