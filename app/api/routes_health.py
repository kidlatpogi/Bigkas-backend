"""
Health check endpoints for the Bigkas backend.
Used by Render and other services to verify the API is running.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["health"]
)


@router.get("")
async def health_check() -> dict:
    """
    Health check endpoint.
    Returns a simple status object to confirm the API is operational.
    """
    return {"status": "ok"}


@router.get("/ping")
async def ping() -> dict:
    """
    Simple ping endpoint for quick connectivity tests.
    """
    return {"ping": "pong"}
