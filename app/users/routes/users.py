from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from pydantic import conint

from app.core.database.db import async_session
from app.utils.response import Responses
from app.users.schemas.users import User, UserBase, UserInDB, UserList
from app.users.actions.users import UsersActions
from app.core.actions import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT,
    MAX_POSTGRES_INTEGER,
)


router = APIRouter(
    prefix="/users",
    dependencies=[Depends(async_session.get_async_session)],
    tags=["users"]
)


@router.get(
    "",
    response_model=list[UserList],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
    },
)
async def get_users(
    skip: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_SKIP,
    limit: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_LIMIT,
    session: AsyncSession = Depends(async_session.get_async_session),
) -> Responses:
    try:
        dataset = await UsersActions().get_users(
            session=session, skip=skip, limit=limit
        )
    except Exception as e:
        return Responses.ResponseBadRequest(message=str(e))
    else:
        dataset = [item.dict() for item in dataset]
        return Responses.ResponseOk(data=dataset)


@router.post(
    "",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad Request",
        }
    },
)
async def create_user(
    user_in: UserBase,
    session: AsyncSession = Depends(async_session.get_async_session),
) -> User:
    user_in = UserInDB(
        name=user_in.name,
        mail=user_in.mail,
    )
    try:
        dataset = await UsersActions().create_user(
            session=session, user_in=user_in
        )
    except Exception as e:
        raise e
    else:
        return Responses.ResponseOk(data=dataset.dict())
