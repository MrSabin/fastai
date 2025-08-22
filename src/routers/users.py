from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr, StringConstraints

from src.config import Settings
from src.dependencies import get_settings
from src.exceptions import ErrorResponse
from src.mocks import mock_get_user, mockable

router = APIRouter(prefix="/users")


class UserDetailsResponse(BaseModel):
    profileId: int
    """User profile ID"""
    email: EmailStr
    """User email"""
    username: Annotated[str, StringConstraints(max_length=255)]
    """Username"""
    registeredAt: datetime
    """User registration date"""
    updatedAt: datetime
    """Last profile update"""
    isActive: bool
    """Is active user"""


@router.get(
    "/me",
    response_model=UserDetailsResponse,
    responses={
        200: {"description": "User details"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    })
@mockable(mock_get_user)
async def get_user(settings: Settings = Depends(get_settings)):
    raise NotImplementedError("Real user implementation not provided")
