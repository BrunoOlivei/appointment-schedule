from datetime import datetime

from pydantic import UUID4, BaseModel, Field


class ScheduleBase(BaseModel):
    created_by: UUID4 = Field(..., description="User ID of the creator")
    parent_govid: str = Field(..., description="Parent's GOVID")
    parent_name: str = Field(..., description="Parent's name")
    start_datetime: datetime = Field(..., description="Start date and time")
    end_datetime: datetime = Field(..., description="End date and time")
    id_type: UUID4 = Field(..., description="Event type ID")
    id_product: UUID4 = Field(None, description="Product ID")


class ScheduleCreate(ScheduleBase):
    id: UUID4 = Field(..., description="Schedule ID")
    scheduled_for: UUID4 = Field(..., description="User ID of the parent")
    implantation_ticket: str = Field(..., description="Implantation ticket")
    meeting_url: str = Field(None, description="Meeting URL")
    id_status: UUID4 = Field(..., description="Status ID")
    deleted: bool = Field(False, description="Deleted flag")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")


class ScheduleForUpdate(BaseModel):
    schedule_for: UUID4 = Field(..., description="User ID of the parent")
    meeting_url: str = Field(None, description="Meeting URL")
    updated_at: datetime = Field(..., description="Update date and time")


class ScheduleStatusUpdate(BaseModel):
    id_status: UUID4 = Field(..., description="Status ID")
    updated_at: datetime = Field(..., description="Update date and time")


class ScheduleUpdate(ScheduleBase):
    scheduled_for: UUID4 = Field(None, description="User ID of the parent")
    meeting_url: str = Field(None, description="Meeting URL")
    id_status: UUID4 = Field(None, description="Status ID")
    deleted: bool = Field(None, description="Deleted flag")
    updated_at: datetime = Field(None, description="Update date and time")


class ScheduleDelete(BaseModel):
    deleted: bool = Field(True, description="Deleted flag")
    deleted_at: datetime = Field(..., description="Deletion date and time")


class Reschedule(ScheduleBase):
    scheduled_for: UUID4 = Field(..., description="User ID of the parent")
    start_datetime: datetime = Field(..., description="Start date and time")
    end_datetime: datetime = Field(..., description="End date and time")
    meeting_url: str = Field(None, description="Meeting URL")
    id_status: UUID4 = Field(..., description="Status ID")
    updated_at: datetime = Field(..., description="Update date and time")


class SchedulePublic(ScheduleBase):
    schedule_for: str = Field(
        ..., description="User name responsible for the event"
    )
    implantation_ticket: str = Field(..., description="Implantation ticket")
    parent_govid: str = Field(..., description="Accountant customer govid")
    parent_name: str = Field(..., description="Accountant customer name")
    start_datetime: datetime = Field(..., description="Start date and time")
    end_datetime: datetime = Field(..., description="End date and time")
    event_type: str = Field(..., description="Event type")
    product: str = Field(None, description="Product")
    meeting_url: str = Field(None, description="Meeting URL")
    status: str = Field(..., description="Event status")


class ListSchedule(SchedulePublic):
    schedules: list[SchedulePublic] = Field(
        ..., description="List of schedules"
    )


class Schedule(ScheduleBase):
    id: UUID4 = Field(..., description="Schedule ID")
    scheduled_for: UUID4 = Field(..., description="User ID of the parent")
    implantation_ticket: str = Field(..., description="Implantation ticket")
    id_type: UUID4 = Field(..., description="Event type ID")
    id_product: UUID4 = Field(None, description="Product ID")
    meeting_url: str = Field(None, description="Meeting URL")
    id_status: UUID4 = Field(..., description="Status ID")
    deleted: bool = Field(False, description="Deleted flag")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: datetime = Field(None, description="Deletion date and time")

    class Config:
        from_attributes = True
