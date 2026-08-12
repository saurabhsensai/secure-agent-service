from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    external_user_id: str
    email: str | None=None
    display_name: str | None=None

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID 
    external_user_id: str
    arcade_user_id: UUID
    email: str | None
    display_name: str | None
    created_at: datetime
    updated_at: datetime
    