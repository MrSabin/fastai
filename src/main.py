from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import Settings
from src.routers.sites import router as sites_router
from src.routers.users import router as users_router

FRONTEND_DIR = Path(__file__).parent / "frontend"


def create_app():
    app = FastAPI()

    app.include_router(users_router, prefix="/frontend-api")
    app.include_router(sites_router, prefix="/frontend-api")

    app.mount(
        "/",
        StaticFiles(directory=FRONTEND_DIR, html=True),
        name="frontend",
    )

    app.state.settings = Settings()

    return app
