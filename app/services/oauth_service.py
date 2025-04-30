from fastapi import Request, HTTPException
from starlette.responses import RedirectResponse, JSONResponse
from app.client.oauth.google import GoogleOAuthClient
from app.client.oauth.kakao import KakaoOAuthClient
from app.client.oauth.github import GithubOAuthClient

CLIENT_MAP = {
    "google": GoogleOAuthClient(),
    "kakao": KakaoOAuthClient(),
    "github": GithubOAuthClient(),
}

async def get_redirect_url(provider: str) -> RedirectResponse:
    """
    주어진 provider에 맞는 소셜 로그인 리다이렉트 URL을 반환한다.
    :param provider
    :return redirect_url
    """
    client = CLIENT_MAP.get(provider)
    if not client:
        raise HTTPException(400, "지원하지 않는 provider입니다.")
    return await client.get_redirect_url()


async def handle_callback(provider: str, request: Request) -> JSONResponse:
    """
    소셜 로그인 후 콜백 요청을 처리하고 사용자 정보를 반환한다.
    :param provider
    :param request
    :return user_info
    """
    client = CLIENT_MAP.get(provider)
    if not client:
        raise HTTPException(400, "지원하지 않는 provider입니다.")

    user_info = await client.process_callback(request)
    return JSONResponse(content=user_info)

