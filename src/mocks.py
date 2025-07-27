def mock_get_user():
    return {
        "profileId": 0,
        "email": "user@example.com",
        "username": "JohnDoe",
        "registeredAt": "string",
        "updatedAt": "string",
        "isActive": True,
    }


def mock_get_user_sites():
    return [{
    "id": 0,
    "title": "MySite",
    "htmlCodeUrl": "https://dvmn.org/media/filer_public/d1/4b/d14bb4e8-d8b4-49cb-928d-fd04ecae46da/index.html",
    "htmlCodeDownloadUrl": "",
    "screenshotUrl": "",
    "prompt": "MyPrompt",
    "createdAt": "string",
    "updatedAt": "string",
    }]
