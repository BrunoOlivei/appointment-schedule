from fastapi import APIRouter

from .permissions import router as permissions_router
from .users import router as users_router
from app.core.config import get_config


config = get_config()

router = APIRouter(prefix=config.API_PREFIX_V1)


router.include_router(permissions_router)
router.include_router(users_router)
