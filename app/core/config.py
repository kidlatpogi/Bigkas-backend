"""
Configuration settings for the Bigkas backend.
"""

from typing import List


class Settings:
    """
    Application settings and configuration.
    Extend this class with database URLs, secrets, and other config as needed.
    """

    # Project metadata
    PROJECT_NAME: str = "Bigkas Backend"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    # CORS Configuration
    # Allowed origins for cross-origin requests
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",   # Vite (React web app)
        "http://localhost:19006",  # Expo (React Native mobile app)
        "http://localhost:3000",   # Alternative dev port
        "https://bigkas-backend.onrender.com",  # Render production backend
    ]
    
    # Render static outbound IPs (for allowlisting in external services)
    # 74.220.52.0/24
    # 74.220.60.0/24

    # Placeholder for future database configuration
    # DATABASE_URL: str = "postgresql://user:password@localhost:5432/bigkas"

    # Placeholder for future secret keys
    # SECRET_KEY: str = "your-secret-key-here"
    # JWT_SECRET: str = "your-jwt-secret-here"

    # Placeholder for ML model configuration
    # MODEL_PATH: str = "./models/vocal_analysis_model.pkl"


# Create a singleton settings instance
settings = Settings()
