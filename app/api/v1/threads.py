from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.exceptions import (
    ThreadNotFoundError,
    UserNotFoundError,
)
from app.schemas.thread import ThreadCreate, ThreadRead
from app.services.thread_service import ThreadService


router = APIRouter(
    prefix="/threads",
    tags=["threads"],
)


@router.post(
    "",
    response_model=ThreadRead,
    status_code=status.HTTP_201_CREATED,
)
def create_thread(
    thread_data: ThreadCreate,
    db: Session = Depends(get_db),
):
    try:
        return ThreadService.create_thread(
            db=db,
            user_id=thread_data.user_id,
            langgraph_thread_id=thread_data.langgraph_thread_id,
        )

    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.get(
    "/{thread_id}",
    response_model=ThreadRead,
)
def get_thread(
    thread_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return ThreadService.get_thread_by_id(
            db=db,
            thread_id=thread_id,
        )

    except ThreadNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )