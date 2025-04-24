from fastapi import APIRouter, Request
from app.services.oauth_service import get_redirect_url, handle_callback

router = APIRouter()

@router.get("/{provider}")
async def oauth_redirect(provider: str, request: Request):
    """
    소셜 로그인 리다이렉트
    :param provider
    :param request
    :return: redirect_url
    """
    return await get_redirect_url(provider)

@router.get("/callback/{provider}")
async def oauth_callback(provider: str, request: Request):
    """
    소셜 로그인 callback
    :param provider
    :param request
    :return:
    """
    return await handle_callback(provider, request)