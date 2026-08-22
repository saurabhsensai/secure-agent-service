from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.exceptions import (
    ThreadNotFoundError,
    UserNotFoundError,
)
from app.models.thread import Thread
from app.models.user import User


class ThreadService:

    @staticmethod
    def create_thread(
        db: Session, 
        user_id: UUID,
        langgraph_thread_id: str | None = None, ) -> Thread:



        user = db.get(User, user_id)

        if user is None:
                raise UserNotFoundError(
                    f"User with id '{user_id}' not found."
                )
        if langgraph_thread_id is None:
                langgraph_thread_id = str(uuid.uuid4())

        thread = Thread(
                user_id=user_id,
                langgraph_thread_id=langgraph_thread_id,
                status="active",
            )

        db.add(thread)
        db.commit()
        db.refresh(thread)

        return thread

    @staticmethod
    def get_thread_by_id(
        db: Session,
        thread_id: UUID,
    ) -> Thread:

        thread = db.get(Thread, thread_id)

        if thread is None:
            raise ThreadNotFoundError(
                f"Thread with id '{thread_id}' not found."
            )

        return thread

    @staticmethod
    def get_threads_by_user(
        db: Session,
        user_id: UUID,
    ) -> list[Thread]:

        user = db.get(User, user_id)

        if user is None:
            raise UserNotFoundError(
                f"User with id '{user_id}' not found."
            )

        # Get all threads belonging to the user
        threads = db.scalars(
            select(Thread)
            .where(Thread.user_id == user_id)
            .order_by(Thread.created_at.desc())
        ).all()

        return list(threads)

    
    @staticmethod
    def update_thread_status(
        db: Session,
        thread_id: UUID,
        new_status: str,
    ) -> Thread:

        thread = db.get(Thread, thread_id)

        if thread is None:
            raise ThreadNotFoundError(
                f"Thread with id '{thread_id}' not found."
            )

        thread.status = new_status

        db.commit()
        db.refresh(thread)

        return thread

