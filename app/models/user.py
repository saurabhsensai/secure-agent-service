import uuid

from sqlalchemy import Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    external_user_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    arcade_user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        default=uuid.uuid4,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    display_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    __table_args__ = (
        Index("ix_users_external_user_id", "external_user_id"),
        Index("ix_users_arcade_user_id", "arcade_user_id"),
    )