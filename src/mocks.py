import asyncio

import aiofiles


def mock_get_user():
    return {
        "profileId": 0,
        "email": "user@example.com",
        "username": "JohnDoe",
        "registeredAt": "2025-06-15T18:29:56+00:00",
        "updatedAt": "2025-06-15T18:29:56+00:00",
        "isActive": True,
    }


def mock_get_user_sites():
    return {
        "sites": [
            {
                "id": 0,
                "title": "MySite",
                "htmlCodeUrl": "https://dvmn.org/media/filer_public/d1/4b/d14bb4e8-d8b4-49cb-928d-fd04ecae46da/index.html",
                "htmlCodeDownloadUrl": "",
                "screenshotUrl": "",
                "prompt": "MyPrompt",
                "createdAt": "2025-06-15T18:29:56+00:00",
                "updatedAt": "2025-06-15T18:29:56+00:00",
            },
        ],
    }


def mock_create_site():
    return {
        "created_at": "2025-06-15T18:29:56+00:00",
        "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
        "html_code_url": "http://example.com/media/index.html",
        "id": 1,
        "prompt": "Сайт любителей играть в домино",
        "screenshot_url": "http://example.com/media/index.png",
        "title": "Фан клуб Домино",
        "updated_at": "2025-06-15T18:29:56+00:00",
    }


async def read_from_file():
    mock_html = "./src/mock_site.html"
    async with aiofiles.open(mock_html) as file:
        async for line in file:
            await asyncio.sleep(0.05)
            yield line.encode("utf-8")
