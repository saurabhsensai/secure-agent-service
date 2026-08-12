from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ThreadCreate(BaseModel):
    user_id: UUID
    langgraph_thread_id: str


class ThreadRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    langgraph_thread_id: str
    status: str
    created_at: datetime
    updated_at: datetime