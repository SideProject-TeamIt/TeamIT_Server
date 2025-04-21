# shared/utils/env_validator.py
import os
import sys
import logging

logger = logging.getLogger(__name__)


def validate_required_env_vars(required_vars, service_name=None):
    """
    필수 환경 변수가 설정되었는지 확인합니다.

    Args:
        required_vars (list): 필수 환경 변수 목록
        service_name (str, optional): 서비스 이름 (로깅용)

    Returns:
        bool: 모든 필수 환경 변수가 설정되었으면 True

    Raises:
        SystemExit: 필수 환경 변수가 누락된 경우 프로그램 종료
    """
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
        if service_name:
            error_msg = f"[{service_name}] {error_msg}"

        logger.error(error_msg)
        print(f"Error: {error_msg}")
        sys.exit(1)

    return True


def get_mongodb_required_vars():
    """MongoDB 서비스에 필요한 환경 변수 목록 반환"""
    return ["MONGO_URI", "MONGO_DB"]


def get_postgres_required_vars():
    """PostgreSQL 서비스에 필요한 환경 변수 목록 반환"""
    return ["POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB"]