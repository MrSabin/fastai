from fastapi import APIRouter

from config import settings
from mocks import mock_get_user_sites
from models.sites import SiteResponse
from models.users import ErrorResponse

router = APIRouter(prefix="/sites")


@router.get(
    "/my",
    response_model=list[SiteResponse],
    responses={
        200: {"description": "User generated sites"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    })
def get_user_sites():
    if settings.USE_MOCKS:
        response = mock_get_user_sites()
        return response
    raise NotImplementedError("Real sites implementation not provided")
