from app.config import settings

def get_version_info():
    return {
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "app_name": settings.APP_NAME
    }
