from fastapi import FastAPI
from typing import Optional, List, Callable, Any
import logging
import time
from .exceptions import register_exception_handlers
from .health import create_health_router

logger = logging.getLogger(__name__)


def create_app(
        app_name: str,
        description: str = "",
        debug: bool = False,
        exception_handlers: bool = True,
        health_check: bool = True,
        db_health_check: Optional[Callable[[], bool]] = None,
        additional_health_checks: Optional[List[Callable[[], Any]]] = None,
        startup_handlers: Optional[List[Callable]] = None,
        shutdown_handlers: Optional[List[Callable]] = None
) -> FastAPI:
    """
    FastAPI 앱을 생성하고 초기화합니다.

    Args:
        app_name: 앱 이름
        description: API 설명
        debug: 디버그 모드 여부
        exception_handlers: 예외 핸들러 등록 여부
        health_check: 헬스체크 엔드포인트 등록 여부
        db_health_check: 데이터베이스 연결 확인 함수
        additional_health_checks: 추가 헬스체크 함수 리스트
        startup_handlers: 앱 시작 시 실행할 핸들러 리스트
        shutdown_handlers: 앱 종료 시 실행할 핸들러 리스트

    Returns:
        초기화된 FastAPI 앱 인스턴스
    """
    app = FastAPI(
        title=app_name,
        description=description,
        debug=debug
    )

    # 예외 핸들러 등록
    if exception_handlers:
        register_exception_handlers(app)

    # 헬스체크 엔드포인트 등록
    if health_check:
        health_router = create_health_router(
            db_check=db_health_check,
            additional_checks=additional_health_checks
        )
        app.include_router(health_router, tags=["monitoring"])

    # 시작 및 종료 이벤트 핸들러 등록
    if startup_handlers:
        for handler in startup_handlers:
            app.add_event_handler("startup", handler)

    if shutdown_handlers:
        for handler in shutdown_handlers:
            app.add_event_handler("shutdown", handler)

    @app.on_event("startup")
    async def log_startup():
        logger.info(f"Starting {app_name} service")

    @app.on_event("shutdown")
    async def log_shutdown():
        logger.info(f"Shutting down {app_name} service")

    return app