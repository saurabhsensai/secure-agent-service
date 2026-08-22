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


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return UserService.create_user(db, user_data)

    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return UserService.get_user_by_id(db, user_id)

    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

        