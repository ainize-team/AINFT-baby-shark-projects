import json
import os
from typing import Callable, Dict, List

from ain.ain import Ain
from fastapi import FastAPI
from loguru import logger

from config import ainetwork_settings, data_settings
from enums import AinetworkProviderURLEnum


def _load_data(app: FastAPI) -> None:
    def make_prompt(
        task_description: str,
        persona: List[str],
        examples: List[Dict[str, str]],
        human: str,
        bot: str,
    ) -> str:
        persona_str = " ".join(persona)
        examples_str = "\n\n".join(
            [
                f"{human}: {example[human]}\n{bot}: {example[bot]}"
                for example in examples
            ]
        )
        return f"{task_description} {persona_str}\n\n{examples_str}"

    app.state.bots = {}
    fn_list = os.listdir(data_settings.data_root_dir)
    logger.info(f"Number of Bot : {len(fn_list)}")
    for fn in fn_list:
        file_path = os.path.join(data_settings.data_root_dir, fn)
        with open(file_path, "r") as f:
            json_obj = json.load(f)
        bot_name = os.path.splitext(fn)[0]
        app.state.bots[bot_name] = {
            "prompt": make_prompt(
                json_obj["task_description"],
                json_obj["persona"],
                json_obj["examples"],
                json_obj["human"],
                json_obj["bot"],
            ),
            "generate_parameters": json_obj["generate_parameters"],
            "human": json_obj["human"],
            "bot": json_obj["bot"],
            "ainft_name": json_obj["ainft_name"],
        }


def _connect_ain(app: FastAPI) -> None:
    logger.info("Connect AINetwork")
    chain_id = (
        0 if ainetwork_settings.provider_url == AinetworkProviderURLEnum.TEST_NET else 1
    )
    app.state.ain = Ain(ainetwork_settings.provider_url, chainId=chain_id)
    app.state.ain.wallet.addAndSetDefaultAccount(ainetwork_settings.ain_private_key)


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running App Start Handler.")
        _load_data(app)
        _connect_ain(app)

    return startup
