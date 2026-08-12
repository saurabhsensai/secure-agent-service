from fastapi import APIrouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}

    