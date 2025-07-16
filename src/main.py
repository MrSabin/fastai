from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, Field

FRONTEND_DIR = Path(__file__).parent / "frontend"
STATIC_FILES_DIR = Path(__file__).parent / "static"

app = FastAPI()
api_router = APIRouter(prefix="/frontend-api")


class ErrorModel(BaseModel):
    detail: str


class UserDetailsResponse(BaseModel):
    profileId: int = Field(description="User profile ID")
    email: EmailStr = Field(description="User email")
    username: str = Field(description="Username", max_length=255)
    registeredAt: str = Field(description="User registration date")
    updatedAt: str = Field(description="Last profile update")
    isActive: bool = Field(description="Is active user")


@api_router.get(
    "/users/me",
    response_model=UserDetailsResponse,
    responses={
        200: {"description": "User details"},
        401: {"model": ErrorModel, "description": "User unauthorized"},
    })
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
