from fastapi import APIRouter

from config import settings
from mocks import mock_get_user
from models.users import ErrorResponse, UserDetailsResponse

router = APIRouter(prefix="/users")


@router.get(
    "/me",
    response_model=UserDetailsResponse,
    responses={
        200: {"description": "User details"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    })
def get_user():
    if settings.USE_MOCKS:
        response = mock_get_user()
        return response
    raise NotImplementedError("Real user implementation not provided")
