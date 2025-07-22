from fastapi import APIRouter

from models.users import ErrorResponse, UserDetailsResponse

router = APIRouter(prefix="/users")


@router.get(
    "/me",
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
