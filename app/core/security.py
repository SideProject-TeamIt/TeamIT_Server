from datetime import datetime, timedelta
from jose import jwt
from fastapi.responses import RedirectResponse
from app.core.config import settings

ALGORITHM = "HS256"

def create_jwt_token(user_id: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    payload = {
        "sub": str(user_id),
        "exp": expire,
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)

def create_login_response(user_id: str) -> RedirectResponse:
    jwt_token = create_jwt_token(user_id)

    response = RedirectResponse(
        url=settings.FRONTEND_URL,
        status_code=302
    )
    response.set_cookie(
        key="access_token",
        value=jwt_token,
        httponly=True,
        secure=False,  # 배포 시 True
        samesite="lax",
        max_age=settings.JWT_EXPIRE_MINUTES * 60,
    )
    return response
