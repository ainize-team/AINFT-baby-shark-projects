from fastapi import APIRouter

from api.v1 import bot


router = APIRouter()

router.include_router(bot.router, prefix="/bot", tags=["bot"])
