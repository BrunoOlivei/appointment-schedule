from fastapi import APIRouter

from .schedule import router as todos_router
from app.core.config import get_config


config = get_config()

router = APIRouter(prefix=config.API_PREFIX_V1)


router.include_router(todos_router)
