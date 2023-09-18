from datetime import datetime

from pydantic import BaseModel, Field

from app.core.schemas.base import BaseInDB
from app.users.models.permissions import Permission


class PermissionBase(BaseModel):
    name: str = Field(..., description="Permission name")


class PermissionInDB(BaseInDB, PermissionBase):
    id: str = Field(..., description="Permission ID")
    is_active: bool = Field(False, description="Permission active flag")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: datetime = Field(None, description="Deletion date and time")

    class Config:
        orm_model = Permission

    def to_orm(self) -> Permission:
        """Converts Pydantic object to SQLAlchemy object, converts
        permission_id to Permission object
        Returns:
            Permission: _description_
        """
        orm_data = dict(self)
        permission_orm = self.Config.orm_model(**orm_data)
        return permission_orm


class PermissionUpdate(BaseModel):
    name: str = Field(..., description="Permission name")
    updated_at: datetime = Field(..., description="Update date and time")


class PermissionDelete(BaseModel):
    is_active: bool = Field(
        True, description="Flag to indicate if the permission is active"
    )
    deleted_at: datetime = Field(..., description="Deletion date and time")


class Permission(PermissionBase):
    id: str = Field(..., description="Permission ID")
    is_active: bool = Field(False, description="Deleted flag")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: datetime = Field(None, description="Deletion date and time")

    class Config:
        from_attributes = True
