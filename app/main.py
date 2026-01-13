"""
Bigkas Backend - FastAPI Application

Main entry point for the Bigkas backend API.
This API serves the Bigkas web (React + Vite) and mobile (React Native + Expo) applications.

To run locally:
    uvicorn app.main:app --reload --port 8000

For Render deployment (production):
    uvicorn app.main:app --host 0.0.0.0 --port 10000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes_health import router as health_router
from app.api.routes_audio import router as audio_router

# Create FastAPI application instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API for Bigkas - Vocal Confidence Analysis Platform",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS middleware
# Allows requests from Vite (web) and Expo (mobile) development servers
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(health_router)
app.include_router(audio_router)


@app.get("/")
async def root() -> dict:
    """
    Root endpoint - provides basic API information.
    """
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "running",
        "docs": "/docs",
        "health": "/health"
    }
