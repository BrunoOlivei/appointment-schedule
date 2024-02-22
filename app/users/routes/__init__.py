from fastapi import APIRouter

from app.core.settings.config import get_config

from .permissions import router as permissions_router
from .users import router as users_router

config = get_config()


router = APIRouter()

router.include_router(users_router)
router.include_router(permissions_router)
