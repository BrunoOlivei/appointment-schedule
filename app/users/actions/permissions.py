from typing import Optional
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from app.core.actions.base import ActionsBase
from app.core.actions.constants import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT
)

from app.users.models.permissions import Permission
from app.users.schemas.permissions import (
    PermissionInDB,
    Permission as PermissionSchema,
    PermissionUpdateActiveInDB
)


class PermissionActions:
    def __init__(self) -> None:
        self._repo = ActionsBase()

    async def get_permissions(
        self,
        session: AsyncSession,
        *,
        skip: int = GET_MULTI_DEFAULT_SKIP,
        limit: int = GET_MULTI_DEFAULT_LIMIT
    ) -> list[Permission]:
        return await self._repo.get_multi(
            session,
            table_model=Permission,
            skip=skip,
            limit=limit,
        )

    async def get_permission_by_name(
        self,
        session: AsyncSession,
        *,
        name: str
    ) -> Permission:
        return await self._repo.get_one(
            session,
            table_model=Permission,
            query_filter=Permission.name == name
        )

    async def create_permission(
        self,
        session: AsyncSession,
        *,
        permission_in: PermissionInDB
    ) -> Permission:
        permissions: list[PermissionSchema] = await self.get_permissions(
            session=session
        )
        print("teste")
        print(permission_in)
        permissions_names = [permission.name for permission in permissions]
        if permission_in.name in permissions_names:
            raise Exception("Permission already exists")
        return await self._repo.create(
            session,
            obj_to_create=permission_in,
        )

    async def update_permission(
        self,
        session: AsyncSession,
        *,
        permission_in: PermissionUpdateActiveInDB
    ) -> Permission:
        permission_to_update: Optional[Permission] = await self._repo.get(
            session,
            table_model=Permission,
            query_filter=Permission.id == permission_in.id
        )
        if not permission_to_update:
            raise Exception("Permission not found")
        if not permission_to_update.is_active:
            raise Exception("Permission is not active")

        permission_in = PermissionUpdateActiveInDB(
            id=permission_to_update.id,
            name=permission_to_update.name,
            is_active=permission_in.is_active,
            created_at=permission_to_update.created_at,
            updated_at=datetime.now(),
            deleted_at=datetime.now() if not permission_in.is_active else None
        )
        return await self._repo.update(
            session,
            updated_obj=permission_in,
            db_obj_to_update=permission_to_update,
        )
