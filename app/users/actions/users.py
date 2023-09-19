from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from app.core.actions.base import ActionsBase
from app.core.actions.constants import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT
)
from app.users.models.users import Users
from app.users.models.permissions import Permission
from app.users.schemas.users import (
    UserInDB,
)


class UsersActions:
    def __init__(self) -> None:
        self._repo = ActionsBase()

    async def get_users(
        self,
        session: AsyncSession,
        *,
        skip: int = GET_MULTI_DEFAULT_SKIP,
        limit: int = GET_MULTI_DEFAULT_LIMIT
    ) -> list[Users]:
        return await self._repo.get_multi(
            session,
            table_model=Users,
            skip=skip,
            limit=limit,
        )

    async def get_user_by_email(
        self,
        session: AsyncSession,
        *,
        email: str
    ) -> Users:
        return await self._repo.get_one(
            session,
            table_model=Users,
            query_filter=Users.email == email
        )

    async def create_user(
        self,
        session: AsyncSession,
        *,
        user_in: UserInDB
    ) -> Users:
        permissions: list[Permission] = await self._repo.get_multi(
            session,
            table_model=Permission
        )
        permissions_names = [permission.name for permission in permissions]
        if user_in.permissions:
            for permission in user_in.permissions:
                if permission.name not in permissions_names:
                    raise Exception("Permission not found")
        return await self._repo.create(
            session,
            obj_to_create=user_in,
        )
