from fastapi import APIRouter, Depends

from src.config import Settings
from src.dependencies import get_settings
from src.mocks import mock_get_user, mockable
from src.models.users import ErrorResponse, UserDetailsResponse

router = APIRouter(prefix="/users")


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
