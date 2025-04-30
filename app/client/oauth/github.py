import httpx
from fastapi import Request, HTTPException
from starlette.responses import RedirectResponse
from app.client.oauth.base import OAuthClient
from app.core.config import settings

GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USERINFO_URL = "https://api.github.com/user"
GITHUB_EMAILS_URL = "https://api.github.com/user/emails"

class GithubOAuthClient(OAuthClient):
    async def get_redirect_url(self) -> RedirectResponse:
        url = (
            f"{GITHUB_AUTH_URL}"
            f"?client_id={settings.GITHUB_CLIENT_ID}"
            f"&redirect_uri={settings.GITHUB_REDIRECT_URI}"
            f"&scope=read:user%20user:email"
        )
        return RedirectResponse(url)

    async def process_callback(self, request: Request) -> dict:
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(400, "Authorization code missing")

        async with httpx.AsyncClient() as client:
            headers = {"Accept": "application/json"}

            # 1. Access token 요청
            token_res = await client.post(
                GITHUB_TOKEN_URL,
                headers=headers,
                data={
                    "client_id": settings.GITHUB_CLIENT_ID,
                    "client_secret": settings.GITHUB_CLIENT_SECRET,
                    "code": code,
                    "redirect_uri": settings.GITHUB_REDIRECT_URI,
                }
            )
            token_res.raise_for_status()
            token_data = token_res.json()

            access_token = token_data.get("access_token")
            if not access_token:
                raise HTTPException(400, f"GitHub access_token 발급 실패: {token_data}")

            # 2. 유저 기본 정보 요청
            userinfo_res = await client.get(
                GITHUB_USERINFO_URL,
                headers={"Authorization": f"Bearer {access_token}"}
            )
            userinfo_res.raise_for_status()
            user = userinfo_res.json()

            # 3. 이메일 정보 요청
            email = user.get("email")
            if not email:
                email_res = await client.get(
                    GITHUB_EMAILS_URL,
                    headers={"Authorization": f"Bearer {access_token}"}
                )
                if email_res.status_code == 403:
                    raise HTTPException(403, "GitHub OAuth scope 부족: user:email 권한이 필요합니다.")

                email_res.raise_for_status()
                emails = email_res.json()
                primary_emails = [e for e in emails if e.get("primary") and e.get("verified")]
                if primary_emails:
                    email = primary_emails[0]["email"]

        if not email:
            raise HTTPException(400, "사용자의 이메일 정보를 확인할 수 없습니다.")

        return {
            "id": user.get("id"),
            "email": email,
            "name": user.get("name"),
            "avatar_url": user.get("avatar_url"),
        }
