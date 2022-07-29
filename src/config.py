from pydantic import BaseSettings, Field

from enums import EnvEnum


class AppSettings(BaseSettings):
    app_name: str = Field("AINFT-BabyShark-Projects", description="FastAPI App Name")
    app_version: str = Field("0.0.1", description="FastAPI App Version")
    app_port: int = Field(8000, ge=0, le=65535, description="FastAPI Server Port")
    app_env: EnvEnum = Field(EnvEnum.DEV, description="FastAPI App Environment")


app_settings = AppSettings()
