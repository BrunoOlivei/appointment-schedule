from datetime import datetime

from pydantic import UUID4, BaseModel, Field


class PermissionUserBase(BaseModel):
    id_user: UUID4 = Field(..., description="User ID")
    id_permission: UUID4 = Field(..., description="Permission ID")


class PermissionUserCreate(PermissionUserBase):
    id: UUID4 = Field(..., description="PermissionUser ID")
    is_active: bool = Field(False, description="PermissionUser active flag")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: datetime = Field(None, description="Deletion date and time")


class PermissionUserUpdate(BaseModel):
    id_permission: UUID4 = Field(..., description="Permission ID")
    updated_at: datetime = Field(..., description="Update date and time")


class PermissionUserDelete(BaseModel):
    is_active: bool = Field(
        True, description="Flag to indicate if the permission_user is active"
    )
    deleted_at: datetime = Field(..., description="Deletion date and time")


class PermissionUser(PermissionUserBase):
    id: UUID4 = Field(..., description="PermissionUser ID")
    is_active: bool = Field(False, description="Deleted flag")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: datetime = Field(None, description="Deletion date and time")

    class Config:
        from_attributes = True
