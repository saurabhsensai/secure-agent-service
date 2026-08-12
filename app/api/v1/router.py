from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.users import router as users_router
from app.api.v1.threads import router as threads_router


router = APIRouter()

router.include_router(health_router)
router.include_router(users_router)
router.include_router(threads_router)