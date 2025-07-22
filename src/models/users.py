from typing import Annotated

from pydantic import BaseModel, EmailStr, StringConstraints


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
