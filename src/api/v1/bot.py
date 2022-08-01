import json
import time
from typing import List

import requests
from fastapi import APIRouter, HTTPException, Request
from loguru import logger

from config import llm_settings
from schemas import UserRequest


router = APIRouter()


@router.post("/chat")
async def chat(request: Request, data: UserRequest):
    bots = request.app.state.bots
    endpoint = llm_settings.llm_endpoint
    if data.bot_name not in bots:
        raise HTTPException(422, f"{data.bot_name} is not found.")
    bot = bots[data.bot_name]
    request_data = bot["generate_parameters"]
    request_data[
        "prompt"
    ] = f"{bot['prompt']}\n\n{bot['human']}: {data.user_message}\n{bot['bot']}:"
    res = requests.post(
        f"{endpoint}/generate",
        headers={"Content-Type": "application/json", "accept": "application/json"},
        data=json.dumps(request_data),
    )
    if res.status_code == 200:
        task_id = res.json()["task_id"]
        logger.info(f"TaskID: {task_id}")
        for i in range(300):
            logger.info(f"Try ({i + 1}/300)")
            res = requests.get(
                f"{endpoint}/result/{task_id}",
                headers={
                    "accept": "application/json",
                },
            )
            if res.status_code == 200 and res.json()["status"] == "completed":
                result = res.json()["result"][0][len(request_data["prompt"]) :]
                ret_text = ""
                for i in range(0, len(result)):
                    if (
                        result[i] == "\n"
                        or result[i:].startswith(f"{bot['human']}:")
                        or result[i:].startswith(f"{bot['bot']}:")
                    ):
                        break
                    ret_text += result[i]
                return ret_text.strip()

            time.sleep(1)
        raise HTTPException(500, "Server Error")
    else:
        logger.error(f"{res.text}")
        raise HTTPException(500, "Server Error")


@router.get("/botList")
async def get_bot_list(request: Request) -> List[str]:
    bots = request.app.state.bots
    return list(bots.keys())


@router.get("/botPrompt")
async def get_bot_prompt(request: Request, bot_name: str) -> str:
    bots = request.app.state.bots
    if bot_name not in bots:
        raise HTTPException(422, f"{bot_name} is not found.")
    return bots[bot_name]["prompt"]
