from datetime import datetime

from pydantic import BaseModel, Field

from typing import Optional, List

from app.core.schemas.base import BaseInDB
from app.users.models.users import Users


class UserBase(BaseModel):
    name: str = Field(..., description="User name")
    mail: str = Field(..., description="User mail")


class PermissionBase(BaseModel):
    id: str = Field(..., description="Permission ID")
    name: str = Field(..., description="Permission name")


class UserCreate(UserBase):
    crm_user_id: int = Field(None, description="User id in crm base")


class UserInDB(BaseInDB, UserCreate):
    id: str = Field(..., description="User ID")
    is_active: bool = Field(
        True, description="Flag to indicate if the user is active")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: Optional[datetime] = Field(
        None, description="Deletion date and time")

    class Config:
        orm_model = Users

    def to_orm(self) -> Users:
        """Converts Pydantic object to SQLAlchemy object, converts
        permission_id to Permission object
        Returns:
            User: _description_
        """
        orm_data = dict(self)
        permissions = orm_data.pop("permissions")
        user_orm = self.Config.orm_model(**orm_data)
        user_orm.permissions = []
        for permission in permissions:
            user_orm.permissions.append(permission.to_orm())
        return user_orm


class UserUpdate(UserBase):
    name: str = Field(None, description="User name")
    mail: str = Field(None, description="User mail")
    updated_at: datetime = Field(
        datetime.utcnow(), description="Update date and time")


class UserList(BaseModel):
    id: str = Field(None, description="User ID")
    crm_user_id: int = Field(None, description="User id in crm base")
    name: str = Field(..., description="User name")
    mail: str = Field(..., description="User mail")
    created_at: datetime = Field(..., description="Creation date and time")


class UserDelete(BaseModel):
    is_active: bool = Field(
        False, description="Flag to indicate if the user is active")
    deleted_at: datetime = Field(..., description="Deletion date and time")


class User(UserBase):
    id: Optional[str] = Field(..., description="User ID")
    crm_user_id: int = Field(None, description="User id in crm base")
    is_active: bool = Field(
        True, description="Flag to indicate if the user is active")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: Optional[datetime] = Field(
        None, description="Deletion date and time")
    permissions: List[PermissionBase] = Field(
        None, description="List of user permissions")

    class Config:
        from_attributes = True
