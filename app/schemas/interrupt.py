from datetime import datetime
from uuid import UUID
from typing import Any

from pydantic import BaseModel, ConfigDict


class InterruptRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    thread_id: UUID
    tool_name: str
    arguments: dict[str, Any]
    status: str
    resolved_at: datetime | None
    created_at: datetime
    updated_at: datetime


class InterruptApprove(BaseModel):
    pass


class InterruptDeny(BaseModel):
    pass