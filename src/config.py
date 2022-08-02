import os
from typing import Union

from pydantic import BaseSettings, Field, HttpUrl

from enums import AinetworkProviderURLEnum, EnvEnum, LLMTypeEnum


class AppSettings(BaseSettings):
    app_name: str = Field("AINFT-BabyShark-Projects", description="FastAPI App Name")
    app_version: str = Field("0.0.1", description="FastAPI App Version")
    app_env: EnvEnum = Field(EnvEnum.DEV, description="FastAPI App Environment")


class LLMSettings(BaseSettings):
    llm_endpoint: HttpUrl = Field(..., description="Large Language Model Endpoint")
    llm_type: LLMTypeEnum = Field(
        LLMTypeEnum.HUGGINGFACE, description="Large Language Model Type"
    )


# TODO: Store Data at Server
class DataSettings(BaseSettings):
    data_root_dir: Union[str, os.PathLike] = Field(
        "./data", description="Path where data stored"
    )


class AiNetworkSettings(BaseSettings):
    provider_url: AinetworkProviderURLEnum = AinetworkProviderURLEnum.TEST_NET
    ain_private_key: str
    ain_address: str


app_settings = AppSettings()
llm_settings = LLMSettings()
data_settings = DataSettings()
ainetwork_settings = AiNetworkSettings()
