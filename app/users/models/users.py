from datetime import datetime
from uuid import uuid4
from pydantic import UUID4

from sqlalchemy import (
    String,
    Boolean,
    UniqueConstraint,
    DateTime,
    PrimaryKeyConstraint,
    UUID,
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)

from app.core.models.base import Base


class Users(Base):
    __tablename__ = "users"

    __table_args__ = (
        UniqueConstraint("mail", name="uq_mail"),
        PrimaryKeyConstraint("id", name="pk_users_id"),
    )
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    mail: Mapped[str] = mapped_column(String(255), nullable=False)
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
    permission = relationship(
        "Permission",
        secondary="permission_users",
        primaryjoin="and_(PermissionUser.id_user == Users.id, PermissionUser.id_permission == Permission.id)",
        secondaryjoin="and_(PermissionUser.id_user == Users.id, PermissionUser.is_active == True)",
    )

    def dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "mail": self.mail,
            "is_active": self.is_active,
        }

    def __repr__(self) -> str:
        return f"<Users id={self.id}>, name={self.name}, mail={self.mail}, created_at={self.created_at}"
