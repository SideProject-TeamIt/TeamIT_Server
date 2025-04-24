import httpx
from fastapi import Request, HTTPException
from starlette.responses import RedirectResponse
from app.core.config import settings
from .base import OAuthClient

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"

class GoogleOAuthClient(OAuthClient):
    async def get_redirect_url(self) -> RedirectResponse:
        url = (
            f"{GOOGLE_AUTH_URL}"
            f"?client_id={settings.GOOGLE_CLIENT_ID}"
            f"&response_type=code"
            f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
            f"&scope=openid%20email%20profile"
        )
        return RedirectResponse(url)

    async def process_callback(self, request: Request) -> dict:
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(400, "Authorization code missing")

        async with httpx.AsyncClient() as client:
            token_res = await client.post(GOOGLE_TOKEN_URL, data={
                "code": code,
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "redirect_uri": settings.GOOGLE_REDIRECT_URI,
                "grant_type": "authorization_code"
            })
            token_res.raise_for_status()
            token_data = token_res.json()

            userinfo_res = await client.get(
                GOOGLE_USERINFO_URL,
                headers={"Authorization": f"Bearer {token_data['access_token']}"}
            )
            userinfo_res.raise_for_status()

        return userinfo_res.json()  # { email, name, picture, ... }
