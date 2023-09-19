from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    String,
    Boolean,
    UniqueConstraint,
    DateTime,
    PrimaryKeyConstraint
)
from sqlalchemy.orm import (
    Mapped, mapped_column
)

from app.core.models.base import Base


class Users(Base):
    __tablename__ = "users"

    __table_args__ = (
        UniqueConstraint("crm_user_id", name="uq_crm_user_id"),
        UniqueConstraint("mail", name="uq_mail"),
        PrimaryKeyConstraint("id", name="pk_users_id"),
    )

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=uuid4
    )
    crm_user_id: Mapped[int] = mapped_column(String(20), nullable=False)
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
    # permissions: Mapped[Optional[List]] = relationship(
    #     "Permission",
    #     secondary="permissons.permission_users",
    #     back_populates="user",
    #     # primaryjoin="Users.id == PermissionUser.id_user",
    # )

    def dict(self):
        return {
            "id": str(self.id),
            "crm_user_id": self.crm_user_id,
            "name": self.name,
            "mail": self.mail,
            "is_active": self.is_active,
        }

    def __repr__(self) -> str:
        return f"<Users id={self.id}>, crm_user_id={self.crm_user_id},\
              name={self.name}, mail={self.mail}, created_at={self.created_at}"
