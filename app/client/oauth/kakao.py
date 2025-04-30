# 파일 위치: app/clients/oauth/kakao.py

import httpx
from fastapi import Request, HTTPException
from starlette.responses import RedirectResponse
from app.client.oauth.base import OAuthClient
from app.core.config import settings

KAKAO_AUTH_URL = "https://kauth.kakao.com/oauth/authorize"
KAKAO_TOKEN_URL = "https://kauth.kakao.com/oauth/token"
KAKAO_USERINFO_URL = "https://kapi.kakao.com/v2/user/me"

class KakaoOAuthClient(OAuthClient):
    async def get_redirect_url(self) -> RedirectResponse:
        url = (
            f"{KAKAO_AUTH_URL}"
            f"?client_id={settings.KAKAO_CLIENT_ID}"
            f"&redirect_uri={settings.KAKAO_REDIRECT_URI}"
            f"&response_type=code"
        )
        return RedirectResponse(url)

    async def process_callback(self, request: Request) -> dict:
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(400, "Authorization code missing")

        async with httpx.AsyncClient() as client:
            token_res = await client.post(
                KAKAO_TOKEN_URL,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": "authorization_code",
                    "client_id": settings.KAKAO_CLIENT_ID,
                    "redirect_uri": settings.KAKAO_REDIRECT_URI,
                    "code": code,
                    "client_secret": settings.KAKAO_CLIENT_SECRET,
                }
            )
            token_res.raise_for_status()
            token_data = token_res.json()

            userinfo_res = await client.get(
                KAKAO_USERINFO_URL,
                headers={"Authorization": f"Bearer {token_data['access_token']}"}
            )
            userinfo_res.raise_for_status()
            user = userinfo_res.json()

        kakao_account = user.get("kakao_account", {})
        profile = kakao_account.get("profile", {})

        return {
            "id": user.get("id"),
            "email": kakao_account.get("email"),
            "nickname": profile.get("nickname"),
            "profile_image": profile.get("profile_image_url"),
        }
