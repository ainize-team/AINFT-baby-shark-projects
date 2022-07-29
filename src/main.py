import uvicorn
from fastapi import FastAPI

from api import router
from config import app_settings
from enums import EnvEnum


def get_app() -> FastAPI:
    fast_api_app = FastAPI(
        title=app_settings.app_name,
        version=app_settings.app_version,
        debug=app_settings.app_env == EnvEnum.DEV,
    )
    fast_api_app.include_router(router)
    return fast_api_app


def main():
    app = get_app()
    uvicorn.run(app=app, host="0.0.0.0", port=app_settings.app_port)


if __name__ == "__main__":
    main()
