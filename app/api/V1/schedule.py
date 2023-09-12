from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from pydantic import conint

from app.core.db import get_async_session
from app.models.response import Responses
from app.schemas.schedule import Schedule
from app.actions import (
    schedule,
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT,
    MAX_POSTGRES_INTEGER
)

router = APIRouter(
    prefix="/schedule",
    dependencies=[Depends(get_async_session)],
    tags=["schedule"]
)


@router.get(
    "",
    response_model=list[Schedule],
    responses={
        status.HTTP_401_UNAUTHORIZED:
        {"description": "Unauthorized"},
    }
)
async def get_schedules(
    parent_govid: str,
    skip: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_SKIP,
    limit: conint(ge=0, le=MAX_POSTGRES_INTEGER) = GET_MULTI_DEFAULT_LIMIT,
    session: AsyncSession = Depends(get_async_session)
) -> list[Schedule]:
    try:
        dataset = await schedule.get_schedules(
            session=session,
            parent_govid=parent_govid,
            skip=skip,
            limit=limit
        )
    except Exception as e:
        raise e
    else:
        dataset = [item.dict() for item in dataset]
        return Responses.ResponseOk(
            data=dataset
        )
