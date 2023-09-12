from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=uuid4
    )
    created_by: Mapped[str] = mapped_column(
        String(36), ForeignKey("user.id"), nullable=False
    )
    scheduled_for: Mapped[str] = mapped_column(
        String(36), ForeignKey("user.id"), nullable=False
    )
    implantation_ticket: Mapped[int] = mapped_column(
        String(20), nullable=False
    )
    parent_govid: Mapped[str] = mapped_column(String(14), nullable=False)
    parent_name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_datetime: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_datetime: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    id_type: Mapped[str] = mapped_column(
        String(36), ForeignKey("event_type.id"), nullable=False
    )
    id_product: Mapped[str] = mapped_column(
        String(36), ForeignKey("product.id"), nullable=True
    )
    meeting_url: Mapped[str] = mapped_column(String(255), nullable=True)
    id_status: Mapped[str] = mapped_column(
        String(36), ForeignKey("status.id"), nullable=False
    )
    deleted: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<Schedule id={self.id}>, parent_govid={self.parent_govid},\
            parent_name={self.parent_name},\
            start_datetime={self.start_datetime},\
            end_datetime={self.end_datetime}, event_type={self.id_type},\
            product={self.id_product}, meeting_url={self.meeting_url},\
            status={self.id_status}"
