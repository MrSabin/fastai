from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

FRONTEND_DIR = Path(__file__).parent / "frontend"
STATIC_FILES_DIR = Path(__file__).parent / "static"

app = FastAPI()
api_router = APIRouter(prefix="/frontend-api")


@api_router.get("/users/me")
def mock_get_user():
    mock_user_data = {
        "profileId": 0,
        "email": "user@example.com",
        "username": "JohnDoe",
        "registeredAt": "string",
        "updatedAt": "string",
        "isActive": True,
    }
    return JSONResponse(content=mock_user_data, status_code=200)


app.include_router(api_router)


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
