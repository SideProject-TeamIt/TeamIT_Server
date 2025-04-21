from fastapi import APIRouter, Depends
from typing import Dict, Any, Callable, List, Optional


def create_health_router(
        db_check: Optional[Callable[[], bool]] = None,
        additional_checks: Optional[List[Callable[[], Dict[str, Any]]]] = None
) -> APIRouter:
    """
    공통 헬스체크 라우터를 생성합니다.

    Args:
        db_check: 데이터베이스 연결 확인 함수
        additional_checks: 추가 헬스체크 함수 리스트

    Returns:
        헬스체크 엔드포인트가 등록된 APIRouter
    """
    router = APIRouter()

    @router.get("/health")
    async def health_check() -> Dict[str, Any]:
        health_status = {
            "status": "healthy"
        }

        # 데이터베이스 체크
        if db_check:
            try:
                health_status["database"] = "connected" if db_check() else "disconnected"
            except Exception as e:
                health_status["database"] = "error"
                health_status["database_error"] = str(e)
                health_status["status"] = "unhealthy"

        # 추가 체크 수행
        if additional_checks:
            for check_func in additional_checks:
                try:
                    check_result = check_func()
                    health_status.update(check_result)
                    if any(v in ["error", "disconnected"] for v in check_result.values()):
                        health_status["status"] = "unhealthy"
                except Exception as e:
                    health_status["status"] = "unhealthy"
                    health_status["error"] = str(e)

        return health_status

    return router