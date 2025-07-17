from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, StringConstraints

FRONTEND_DIR = Path(__file__).parent / "frontend"
STATIC_FILES_DIR = Path(__file__).parent / "static"

app = FastAPI()
api_router = APIRouter(prefix="/frontend-api")


class ErrorResponse(BaseModel):
    detail: str


class UserDetailsResponse(BaseModel):
    profileId: int
    """User profile ID"""
    email: EmailStr
    """User email"""
    username: Annotated[str, StringConstraints(max_length=255)]
    """Username"""
    registeredAt: str
    """User registration date"""
    updatedAt: str
    """Last profile update"""
    isActive: bool
    """Is active user"""


@api_router.get(
    "/users/me",
    response_model=UserDetailsResponse,
    responses={
        200: {"description": "User details"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    })
def mock_get_user():
    return {
        "profileId": 0,
        "email": "user@example.com",
        "username": "JohnDoe",
        "registeredAt": "string",
        "updatedAt": "string",
        "isActive": True,
    }


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
