from fastapi import APIRouter

from app.users.routes import router as users_router
from .settings.config import get_config

config = get_config()

router = APIRouter(prefix=config.API_PREFIX_V1)

router.include_router(users_router)