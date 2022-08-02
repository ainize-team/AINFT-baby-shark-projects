import os

from fastapi import APIRouter, Request

from config import ainetwork_settings
from schemas import ServerStatus

from . import v1


router = APIRouter()
router.include_router(v1.router, prefix="/v1")


@router.get("/")
async def get_server_status(request: Request) -> ServerStatus:
    bots = request.app.state.bots
    return ServerStatus(
        number_of_workers=os.getenv("NUMBER_OF_WORKERS", 1),
        number_of_bot=len(list(bots.keys())),
        ain_provider_url=ainetwork_settings.ain_provider_url,
    )
