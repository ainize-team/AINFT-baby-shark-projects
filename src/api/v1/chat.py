from fastapi import APIRouter

from schemas import UserRequest


router = APIRouter()


@router.post("/chat")
async def chat(text: UserRequest):
    return text
