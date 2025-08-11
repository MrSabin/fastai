from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from html_page_generator import AsyncDeepseekClient, AsyncUnsplashClient

from src.config import Settings
from src.routers.sites import router as sites_router
from src.routers.users import router as users_router

FRONTEND_DIR = Path(__file__).parent / "frontend"


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings: Settings = app.state.settings

    async with (
        AsyncDeepseekClient.setup(
            deepseek_api_key=settings.DEEPSEEK.API_KEY,
            deepseek_base_url=settings.DEEPSEEK.BASE_URL,
        ),
        AsyncUnsplashClient.setup(
            unsplash_client_id=settings.UNSPLASH.API_KEY,
            timeout=settings.UNSPLASH.TIMEOUT,
        ),
    ):
        app.state.deepseek_client = AsyncDeepseekClient.get_initialized_instance()
        app.state.unsplash_client = AsyncUnsplashClient.get_initialized_instance()

        yield


def create_app():
    app = FastAPI(lifespan=lifespan)

    app.state.settings = Settings()

    app.include_router(users_router, prefix="/frontend-api")
    app.include_router(sites_router, prefix="/frontend-api")

    app.mount(
        "/",
        StaticFiles(directory=FRONTEND_DIR, html=True),
        name="frontend",
    )

    return app
