from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from pydantic import conint

from app.core.db import get_async_session
from app.utils.response import Responses
from app.users.schemas.users import User, UserBase, UserInDB
from app.users.actions.users import UsersActions
from app.users.actions import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT,
    MAX_POSTGRES_INTEGER,
)

router = APIRouter(
    prefix="/users",
    dependencies=[Depends(get_async_session)],
    tags=["users"]
)


@router.get(
    "",
    response_model=list[User],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
    },
)
async def get_schedules(
    parent_govid: str,
    skip: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_SKIP,
    limit: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_LIMIT,
    session: AsyncSession = Depends(get_async_session),
) -> list[User]:
    try:
        dataset = await UsersActions().get_schedules(
            session=session, parent_govid=parent_govid, skip=skip, limit=limit
        )
    except Exception as e:
        raise e
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
async def create_schedule(
    user_in: UserBase,
    session: AsyncSession = Depends(get_async_session),
) -> User:
    user_in = UserInDB(
        id=str(uuid4()),
        crm_user_id=user_in.crm_user_id,
        name=user_in.name,
        email=user_in.email,
        is_active=True,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
