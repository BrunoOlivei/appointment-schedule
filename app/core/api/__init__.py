from fastapi import APIRouter

from ...users.api.V1 import router as v1_router


router = APIRouter()
router.include_router(v1_router)