from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from config import settings
from mocks import mock_create_site, mock_get_user_sites, read_from_file
from models.sites import CreateSiteRequest, SiteGenerationRequest, SiteResponse
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


@router.post(
    "/create",
    response_model=SiteResponse,
    responses={
        200: {"description": "Site created succesfully"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    },
)
def create_site(request: CreateSiteRequest):
    if settings.USE_MOCKS:
        response = mock_create_site()
        return response
    raise NotImplementedError("Real sites implementation not provided")


@router.post(
    "/{site_id}/generate",
    responses={
        200: {
            "description": "Site generation succesfully started",
            "content": {"text/plain": {"schema": {"type": "string"}}},
        },
    },
)
async def generate_site(site_id: int, request: SiteGenerationRequest | None = None):
    if settings.USE_MOCKS:
        return StreamingResponse(
            read_from_file(),
            media_type="text/csv",
        )
    raise NotImplementedError("Real site generation not implemented")


@router.get(
    "/{site_id}",
    response_model=SiteResponse,
)
def get_site(site_id: int):
    if settings.USE_MOCKS:
        response = mock_create_site()
        return response
    raise NotImplementedError("Not yet...")
