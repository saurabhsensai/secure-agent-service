from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])


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