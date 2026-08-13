from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    user = User(
        external_user_id=user_data.external_user_id,
        email=user_data.email,
        display_name=user_data.display_name,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user