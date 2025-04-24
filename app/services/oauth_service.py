from fastapi import Request, HTTPException
from starlette.responses import RedirectResponse, JSONResponse
from app.client.oauth.google import GoogleOAuthClient

CLIENT_MAP = {
    "google": GoogleOAuthClient(),
    # "kakao": KakaoOAuthClient(),
    # "github": GithubOAuthClient(),
}

async def get_redirect_url(provider: str) -> RedirectResponse:
    """
    리다이렉트 url 생성
    :param provider
    :return: redirect_url
    """
    client = CLIENT_MAP.get(provider)
    if not client:
        raise HTTPException(400, "지원하지 않는 provider입니다.")
    return await client.get_redirect_url()

async def handle_callback(provider: str, request: Request) -> JSONResponse:
    """
    회원 정보 callback 함수
    :param provider
    :param request
    :return: user_info
    """
    client = CLIENT_MAP.get(provider)
    if not client:
        raise HTTPException(400, "지원하지 않는 provider입니다.")

    user_info = await client.process_callback(request)

    return JSONResponse(content=user_info)
