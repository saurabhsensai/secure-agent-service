from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import (
    InterruptAlreadyResolvedError,
    InterruptNotFoundError,
    ThreadNotFoundError,
)
from app.models.interrupt import Interrupt
from app.models.thread import Thread


class InterruptService:

    @staticmethod
    def create_interrupt(
        db: Session,
        thread_id: UUID,
        tool_name: str,
        arguments: dict,
    ) -> Interrupt:

        thread = db.get(Thread, thread_id)

        if thread is None:
            raise ThreadNotFoundError(
                f"Thread with id '{thread_id}' not found."
            )

        # Create the interrupt
        interrupt = Interrupt(
            thread_id=thread_id,
            tool_name=tool_name,
            arguments=arguments,
            status="pending",
        )

        db.add(interrupt)

        thread.status = "waiting_approval"

        db.commit()
        db.refresh(interrupt)

        return interrupt

    @staticmethod
    def get_interrupt_by_id(
        db: Session,
        interrupt_id: UUID,
    ) -> Interrupt:

        interrupt = db.get(Interrupt, interrupt_id)

        if interrupt is None:
            raise InterruptNotFoundError(
                f"Interrupt with id '{interrupt_id}' not found."
            )

        return interrupt

    @staticmethod
    def get_pending_interrupts(
        db: Session,
        thread_id: UUID | None = None,
    ) -> list[Interrupt]:

        query = select(Interrupt).where(
            Interrupt.status == "pending"
        )

        if thread_id is not None:
            query = query.where(
                Interrupt.thread_id == thread_id
            )

        interrupts = db.scalars(
            query.order_by(Interrupt.created_at.asc())
        ).all()

        return list(interrupts)

    @staticmethod
    def approve_interrupt(
        db: Session,
        interrupt_id: UUID,
    ) -> Interrupt:

        interrupt = db.get(Interrupt, interrupt_id)

        if interrupt is None:
            raise InterruptNotFoundError(
                f"Interrupt with id '{interrupt_id}' not found."
            )

        if interrupt.status != "pending":
            raise InterruptAlreadyResolvedError(
                f"Interrupt '{interrupt_id}' has already been resolved."
            )

        interrupt.status = "approved"
        interrupt.resolved_at = datetime.now(timezone.utc)

        thread = db.get(Thread, interrupt.thread_id)

        if thread is not None:
            thread.status = "active"

        db.commit()
        db.refresh(interrupt)

        return interrupt

    @staticmethod
    def deny_interrupt(
        db: Session,
        interrupt_id: UUID,
    ) -> Interrupt:

        interrupt = db.get(Interrupt, interrupt_id)

        if interrupt is None:
            raise InterruptNotFoundError(
                f"Interrupt with id '{interrupt_id}' not found."
            )

        # Only pending interrupts can be denied
        if interrupt.status != "pending":
            raise InterruptAlreadyResolvedError(
                f"Interrupt '{interrupt_id}' has already been resolved."
            )

        interrupt.status = "denied"
        interrupt.resolved_at = datetime.now(timezone.utc)

        thread = db.get(Thread, interrupt.thread_id)

        if thread is not None:
            thread.status = "active"

        db.commit()
        db.refresh(interrupt)

        return interrupt