from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.exceptions import (
    InterruptAlreadyResolvedError,
    InterruptNotFoundError,
)
from app.schemas.interrupt import InterruptRead
from app.services.interrupt_service import InterruptService


router = APIRouter(
    prefix="/interrupts",
    tags=["interrupts"],
)


@router.get(
    "",
    response_model=list[InterruptRead],
)
def get_pending_interrupts(
    thread_id: UUID | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return InterruptService.get_pending_interrupts(
        db=db,
        thread_id=thread_id,
    )


@router.get(
    "/{interrupt_id}",
    response_model=InterruptRead,
)
def get_interrupt(
    interrupt_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return InterruptService.get_interrupt_by_id(
            db=db,
            interrupt_id=interrupt_id,
        )

    except InterruptNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.post(
    "/{interrupt_id}/approve",
    response_model=InterruptRead,
)
def approve_interrupt(
    interrupt_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return InterruptService.approve_interrupt(
            db=db,
            interrupt_id=interrupt_id,
        )

    except InterruptNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

    except InterruptAlreadyResolvedError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.post(
    "/{interrupt_id}/deny",
    response_model=InterruptRead,
)
def deny_interrupt(
    interrupt_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        return InterruptService.deny_interrupt(
            db=db,
            interrupt_id=interrupt_id,
        )

    except InterruptNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

    except InterruptAlreadyResolvedError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )