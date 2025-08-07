from fastapi import APIRouter, Depends

from src.dependencies import get_settings
from src.mocks import mock_get_user
from src.models.users import ErrorResponse, UserDetailsResponse

router = APIRouter(prefix="/users")


@router.get(
    "/me",
    response_model=UserDetailsResponse,
    responses={
        200: {"description": "User details"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    })
def get_user(settings=Depends(get_settings)):
    if settings.USE_MOCKS:
        response = mock_get_user()
        return response
    raise NotImplementedError("Real user implementation not provided")
