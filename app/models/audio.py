"""
Pydantic models for audio analysis endpoints.
"""

from pydantic import BaseModel, Field


class AudioAnalysisResponse(BaseModel):
    """
    Response model for audio analysis results.
    """

    session_id: str = Field(
        ...,
        description="Unique identifier for the analysis session"
    )
    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Vocal confidence score from 0 to 100"
    )
    message: str = Field(
        ...,
        description="Human-readable message about the analysis result"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "abc123-def456-ghi789",
                "confidence_score": 75.5,
                "message": "Audio analysis completed successfully"
            }
        }
