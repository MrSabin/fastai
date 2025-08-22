from datetime import datetime

from anyio import CancelScope
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from html_page_generator import AsyncPageGenerator
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel as convert_to_camel

from src.config import Settings
from src.dependencies import get_settings
from src.exceptions import ErrorResponse
from src.mocks import mock_create_site, mock_get_user_sites, mockable, read_from_file

router = APIRouter(prefix="/sites")


class Site(BaseModel):
    id: int
    """Site ID"""
    title: str
    """Site title"""
    html_code_url: str | None
    """Site HTML code URL"""
    html_code_download_url: str | None
    """Site HTML code URL in S3Bucket"""
    screenshot_url: str | None
    """Site screenshot URL"""
    prompt: str
    """Prompt used for generate site"""
    created_at: datetime
    """Site creation timestamp"""
    updated_at: datetime
    """Site last update timestamp"""

    model_config = ConfigDict(
        alias_generator=convert_to_camel,
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "id": 1,
                    "title": "Фан клуб Домино",
                    "html_code_url": "http://example.com/media/index.html",
                    "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
                    "screenshot_url": "http://example.com/media/index.png",
                    "prompt": "Сайт любителей играть в домино",
                    "created_at": "2025-06-15T18:29:56+00:00",
                    "updated_at": "2025-06-15T18:29:56+00:00",
                },
            ],
        },
    )


class SitesResponse(BaseModel):
    sites: list[Site]
    """User generated sites list"""


class CreateSiteRequest(BaseModel):
    title: str | None = None
    """Site title"""
    prompt: str
    """Prompt for generate site"""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "title": "Фан клуб игры в домино",
                    "prompt": "Сайт любителей играть в домино",
                },
            ],
        },
    )


class SiteGenerationRequest(BaseModel):
    prompt: str
    """Prompt for generate site"""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "prompt": "Сайт любителей играть в домино",
                },
            ],
        },
    )


@router.get(
    "/my",
    response_model=SitesResponse,
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
) -> StreamingResponse:

    if settings.USE_MOCKS:
        return StreamingResponse(
            read_from_file(),
            media_type="text/plain",
        )
    generator = AsyncPageGenerator(debug_mode=settings.DEEPSEEK.DEBUG_MODE)
    user_prompt = request.prompt

    async def generate_content():
        with CancelScope(shield=True):
            async for chunk in generator(user_prompt):
                yield chunk

    return StreamingResponse(
        generate_content(),
        media_type="text/plain",
    )


@router.get(
    "/{site_id}",
    response_model=Site,
)
@mockable(mock_create_site)
async def get_site(site_id: int, settings: Settings = Depends(get_settings)):
    raise NotImplementedError("Not yet...")
