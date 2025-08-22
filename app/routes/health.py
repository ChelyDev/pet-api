#health check

from fastapi import APIRouter

router = APIRouter()
#endpoint health check
@router.get("/health")
def health_check():
    return {"status": "healthy"}

    """
    Health check endpoint to verify if the service is running.
    """