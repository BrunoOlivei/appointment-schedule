from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from pydantic import conint

from app.core.database.db import async_session
from app.utils.response import Responses
from app.users.schemas.permissions import (
    Permission, PermissionBase, PermissionInDB, PermissionUpdateActive
)
from app.users.actions.permissions import PermissionActions
from app.core.actions import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT,
    MAX_POSTGRES_INTEGER,
)


router = APIRouter(
    prefix="/permission",
    dependencies=[Depends(async_session.get_async_session)],
    tags=["permission"]
)


@router.get(
    "",
    response_model=list[Permission],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
    },
)
async def get_permissions(
    skip: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_SKIP,
    limit: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_LIMIT,
    session: AsyncSession = Depends(async_session.get_async_session),
) -> list[Permission]:
    try:
        dataset = await PermissionActions().get_permissions(
            session=session, skip=skip, limit=limit
        )
    except Exception as e:
        return Responses.ResponseError(data=e)
    else:
        dataset = [item.dict() for item in dataset]
        return Responses.ResponseOk(data=dataset)


@router.post(
    "",
    response_model=Permission,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad Request",
        }
    },
)
async def create_permission(
    permission_in: PermissionBase,
    session: AsyncSession = Depends(async_session.get_async_session),
) -> Permission:
    permission_in = PermissionInDB(
        id=str(uuid4()),
        name=permission_in.name,
        is_active=True,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    try:
        dataset = await PermissionActions().create_permission(
            session=session, permission_in=permission_in
        )
    except Exception as e:
        return Responses.ResponseError(data=e)
    else:
        return Responses.ResponseOk(data=dataset.dict())


@router.put(
    "",
    response_model=Permission,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad Request",
        }
    },
)
async def update_permission(
    permission_in: PermissionUpdateActive,
    session: AsyncSession = Depends(async_session.get_async_session),
) -> Permission:

    try:
        dataset = await PermissionActions().update_permission(
            session=session,
            permission_in=permission_in
        )
    except Exception as e:
        return Responses.ResponseError(data=e)
    else:
        return Responses.ResponseOk(data=dataset.dict())
