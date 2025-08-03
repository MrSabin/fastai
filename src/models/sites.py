from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class SiteResponse(BaseModel):
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
    created_at: str
    """Site creation timestamp"""
    updated_at: str
    """Site last update timestamp"""

    model_config = ConfigDict(
        alias_generator=to_camel,
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


class CreateSiteRequest(BaseModel):
    title: str | None = None
    """Site title"""
    prompt: str
    """Prompt for generate site"""

    model_config = ConfigDict(
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
        json_schema_extra={
            "examples": [
                {
                    "prompt": "Сайт любителей играть в домино",
                },
            ],
        },
    )
