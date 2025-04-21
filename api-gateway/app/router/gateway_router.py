from fastapi import APIRouter, Request, HTTPException, Response
import httpx
from ..config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.api_route("/{service_name}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def route_request(service_name: str, path: str, request: Request):
    # 서비스 URL 매핑
    service_urls = {
        "auth": settings.AUTH_SERVICE_URL,
        "user": settings.USER_SERVICE_URL,
        "team": settings.TEAM_SERVICE_URL,
        "project": settings.PROJECT_SERVICE_URL,
        "notification": settings.NOTIFICATION_SERVICE_URL
    }

    if service_name not in service_urls:
        raise HTTPException(status_code=404, detail=f"Service '{service_name}' not found")

    # 목적지 URL 구성
    target_url = f"{service_urls[service_name]}/{path}"
    logger.debug(f"Routing request to: {target_url}")

    # 요청 본문과 헤더 추출
    body = await request.body()
    headers = dict(request.headers)

    # content-length 제거 (httpx가 자동으로 계산)
    headers.pop("content-length", None)
    headers.pop("host", None)

    # 타임아웃 설정 (기본 5초)
    timeout = httpx.Timeout(5.0)

    try:
        # 요청 전달
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                content=body
            )

        # 응답 반환 (헤더 포함)
        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=dict(response.headers)
        )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Service request timed out")
    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"Error communicating with service: {str(e)}")


@router.get("/health")
def health_check():
    return {"status": "ok"}