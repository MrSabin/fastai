from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from html_page_generator import AsyncPageGenerator

from src.config import Settings
from src.dependencies import get_settings
from src.mocks import mock_create_site, mock_get_user_sites, mockable, read_from_file
from src.models.sites import CreateSiteRequest, Site, SiteGenerationRequest, Sites
from src.models.users import ErrorResponse

router = APIRouter(prefix="/sites")


@router.get(
    "/my",
    response_model=Sites,
    responses={
        200: {"description": "User generated sites"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    })
@mockable(mock_get_user_sites)
async def get_user_sites(settings: Settings = Depends(get_settings)):
    raise NotImplementedError("Real sites implementation not provided")


@router.post(
    "/create",
    response_model=Site,
    responses={
        200: {"description": "Site created succesfully"},
        401: {"model": ErrorResponse, "description": "User unauthorized"},
    },
)
@mockable(mock_create_site)
async def create_site(request: CreateSiteRequest, settings: Settings = Depends(get_settings)):
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
async def generate_site(
    site_id: int,
    request: SiteGenerationRequest,
    settings: Settings = Depends(get_settings),
):
    if settings.USE_MOCKS:
        return StreamingResponse(
            read_from_file(),
            media_type="text/plain",
        )
    generator = AsyncPageGenerator()
    user_prompt = request.prompt
    return StreamingResponse(
        generator(user_prompt),
        media_type="text/plain",
    )


@router.get(
    "/{site_id}",
    response_model=Site,
)
@mockable(mock_create_site)
async def get_site(site_id: int, settings: Settings = Depends(get_settings)):
    raise NotImplementedError("Not yet...")
