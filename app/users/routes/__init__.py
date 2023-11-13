from fastapi import APIRouter

from .permissions import router as permissions_router
from .users import router as users_router
from app.core.settings.config import get_config


config = get_config()


router = APIRouter(prefix="/users")

router.include_router(users_router)
router.include_router(permissions_router)
