from fastapi import FastAPI

from app.api.v1.router import router as v1_router


app = FastAPI(
    title="Secure Agent Service",
    description="API service for secure, human-in-the-loop AI agent interactions.",
    version="1.0.0",
)

app.include_router(
    v1_router,
    prefix="/api/v1",
)