from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.users import router as users_router

FRONTEND_DIR = Path(__file__).parent / "frontend"
STATIC_FILES_DIR = Path(__file__).parent / "static"

app = FastAPI()


app.include_router(users_router, prefix="/frontend-api")


app.mount(
    "/static",
    StaticFiles(directory=STATIC_FILES_DIR),
    name="static-files",
)

app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend",
)
