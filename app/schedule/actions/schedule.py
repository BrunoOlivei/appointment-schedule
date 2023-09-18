from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from app.core.actions.base import ActionsBase
from app.core.actions.constants import (
    GET_MULTI_DEFAULT_SKIP,
    GET_MULTI_DEFAULT_LIMIT
)
from app.schedule.models.tables import Schedule


class ScheduleActions:
    def __init__(self) -> None:
        self._repo = ActionsBase()

    async def get_schedules(
        self,
        session: AsyncSession,
        *,
        parent_govid: str,
        skip: int = GET_MULTI_DEFAULT_SKIP,
        limit: int = GET_MULTI_DEFAULT_LIMIT
    ) -> list[Schedule]:
        return await self._repo.get_multi(
            session,
            table_model=Schedule,
            query_filter=Schedule.parent_govid == parent_govid,
            skip=skip,
            limit=limit,
        )

    async def create_schedule(
        self,
        session: AsyncSession,
        *,
        schedule_in: Schedule
    ) -> Schedule:
        return await self._repo.create(
            session,
            table_model=Schedule,
            data=schedule_in
        )


schedule = ScheduleActions()
