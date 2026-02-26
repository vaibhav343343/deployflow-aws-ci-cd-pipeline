from fastapi import APIRouter
from app.services.version import get_version_info
from datetime import datetime

router = APIRouter()

@router.get("/")
async def root():
    return {
        "message": "Welcome to DeployFlow API",
        "status": "operational"
    }

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/version")
async def version():
    return get_version_info()
