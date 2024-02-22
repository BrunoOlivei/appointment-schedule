from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from app.core.schemas.base import BaseInDB
from app.users.models.users import Users


class UserBase(BaseModel):
    name: str = Field(
        ...,
        title="User name",
        description="User name",
        max_length=255,
        min_length=3,
    )
    mail: str = Field(
        ...,
        title="User mail",
        description="User mail",
        max_length=255,
        min_length=3,
    )
    permission: Optional[List[str]] = Field(
        None,
        title="User permissions",
        description="List of user permissions ids",
        example=["78FBC6E6-9D68-4567-B82C-CAE1AFE2F05F"],
    )


class PermissionBase(BaseModel):
    id: str = Field(..., description="Permission ID")
    name: str = Field(..., description="Permission name")


class UserInDB(BaseInDB, UserBase):
    id: str = Field(
        default_factory=lambda: uuid4().__str__(),
        title="Unique identifier",
        description="Unique identifier for the user",
        example="78FBC6E6-9D68-4567-B82C-CAE1AFE2F05F",
    )
    is_active: bool = Field(
        True,
        title="Active flag",
        description="Flag to indicate if the user is active",
    )
    created_at: datetime = Field(
        datetime.utcnow(),
        title="Creation date and time",
        description="Creation date and time",
        example=datetime.utcnow(),
    )

    class Config:
        orm_model = Users

    def to_orm(self) -> Users:
        """Converts Pydantic object to SQLAlchemy object, converts
        permission_id to Permission object
        Returns:
            User: _description_
        """
        orm_data = dict(self)
        print(orm_data)
        permissions = orm_data.pop("permission")
        user_orm = self.Config.orm_model(**orm_data)
        user_orm.permission = []
        for permission in permissions:
            user_orm.permission.append(permission.to_orm())
        return user_orm


class UserUpdate(UserBase):
    name: str = Field(None, description="User name")
    mail: str = Field(None, description="User mail")
    updated_at: datetime = Field(datetime.utcnow(), description="Update date and time")


class UserList(BaseModel):
    id: str = Field(None, description="User ID")
    name: str = Field(..., description="User name")
    mail: str = Field(..., description="User mail")
    created_at: datetime = Field(..., description="Creation date and time")


class UserDelete(BaseModel):
    is_active: bool = Field(False, description="Flag to indicate if the user is active")
    deleted_at: datetime = Field(..., description="Deletion date and time")


class User(UserBase):
    id: Optional[str] = Field(..., description="User ID")
    is_active: bool = Field(True, description="Flag to indicate if the user is active")
    created_at: datetime = Field(..., description="Creation date and time")
    updated_at: datetime = Field(..., description="Update date and time")
    deleted_at: Optional[datetime] = Field(None, description="Deletion date and time")
    permissions: List[PermissionBase] = Field(
        None, description="List of user permissions"
    )

    class Config:
        from_attributes = True
