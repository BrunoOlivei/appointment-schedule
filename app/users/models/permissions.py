from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    ForeignKey,
    String,
    Boolean,
    UniqueConstraint,
    DateTime,
    PrimaryKeyConstraint,
    ForeignKeyConstraint
)
from sqlalchemy.orm import (
    Mapped, mapped_column
)

from app.core.models.base import Base


class Permission(Base):
    __tablename__ = "permission"

    __table_args__ = (
        UniqueConstraint("name", name="uq_permission_name"),
        PrimaryKeyConstraint("id", name="pk_permission_id"),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    # user: Mapped[Optional[List]] = relationship(
    #     "Users",
    #     secondary="permissons.permission_users",
    #     back_populates="permissions",
    #     # primaryjoin="Permission.id == PermissionUser.id_permission",
    # )

    def dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }

    def __repr__(self) -> str:
        return f"<Permission id={self.id},\
            name={self.name}, created_at={self.created_at}>"


class PermissionUser(Base):
    __tablename__ = "permission_users"

    __table_args__ = (
        UniqueConstraint(
            "id", name="uq_permission_users_id"
        ),
        PrimaryKeyConstraint("id", name="pk_permission_users_id"),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=uuid4
    )
    id_user: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=False
    )
    ForeignKeyConstraint(
        ["id_user"],
        ["users.id"],
        name="fk_permission_users_id_user",
    )
    id_permission: Mapped[str] = mapped_column(
        String(36), ForeignKey("permission.id"), nullable=False
    )
    ForeignKeyConstraint(
        ["id_permission"],
        ["permission.id"],
        name="fk_permission_users_id_permission",
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<Permission id={self.id}>, id_user={self.id_user},\
            id_permission={self.id_permission},\
            created_at={self.created_at}"
