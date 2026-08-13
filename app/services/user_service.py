from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from app.models.user import User
from app.schemas.user import UserCreate

class UserService:

    @staticmethod
    def create_user(
        db: Session,
        user_data: UserCreate,
    ) -> User:
        # Check whether the user already exists
        existing_user = db.scalar(
            select(User).where(
                User.external_user_id == user_data.external_user_id
            )
        )

        if existing_user:
            raise UserAlreadyExistsError(
                f"User with external_user_id "
                f"'{user_data.external_user_id}' already exists."
            )

        # Create user
        user = User(
            external_user_id=user_data.external_user_id,
            email=user_data.email,
            display_name=user_data.display_name,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: UUID,
    ) -> User:
        user = db.get(User, user_id)

        if user is None:
            raise UserNotFoundError(
                f"User with id '{user_id}' not found."
            )

        return user

    @staticmethod
    def get_user_by_external_id(
        db: Session,
        external_user_id: str,
    ) -> User:
        user = db.scalar(
            select(User).where(
                User.external_user_id == external_user_id
            )
        )

        if user is None:
            raise UserNotFoundError(
                f"User with external_user_id "
                f"'{external_user_id}' not found."
            )

        return user


        