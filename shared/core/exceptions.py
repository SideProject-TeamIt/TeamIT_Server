from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Dict, Any, Type, Optional, List
from pydantic import BaseModel


class APIError(Exception):
    """기본 API 에러 클래스"""
    status_code: int = 500
    code: str = "internal_error"
    message: str = "An internal error occurred"

    def __init__(self, message: Optional[str] = None, details: Optional[Dict[str, Any]] = None):
        self.message = message or self.message
        self.details = details or {}
        super().__init__(self.message)


class NotFoundError(APIError):
    status_code = 404
    code = "not_found"
    message = "Resource not found"


class ValidationError(APIError):
    status_code = 422
    code = "validation_error"
    message = "Validation error"


class AuthenticationError(APIError):
    status_code = 401
    code = "authentication_error"
    message = "Authentication required"


class AuthorizationError(APIError):
    status_code = 403
    code = "authorization_error"
    message = "Not authorized"


class ErrorResponse(BaseModel):
    code: str
    message: str
    details: Dict[str, Any] = {}


def register_exception_handlers(app: FastAPI, additional_exceptions: Optional[List[Type[APIError]]] = None):
    """
    FastAPI 앱에 예외 핸들러를 등록합니다.

    Args:
        app: FastAPI 앱 인스턴스
        additional_exceptions: 추가 예외 클래스 리스트
    """
    exceptions = [APIError, NotFoundError, ValidationError, AuthenticationError, AuthorizationError]
    if additional_exceptions:
        exceptions.extend(additional_exceptions)

    for exc in exceptions:
        app.add_exception_handler(exc, create_exception_handler(exc))


def create_exception_handler(exc_class: Type[APIError]):
    """특정 예외 클래스에 대한 핸들러를 생성합니다."""

    async def handler(request: Request, exc: exc_class) -> JSONResponse:
        response = ErrorResponse(
            code=exc.code,
            message=exc.message,
            details=exc.details
        )
        return JSONResponse(
            status_code=exc.status_code,
            content=response.dict()
        )

    return handler