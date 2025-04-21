from typing import Dict, Optional
import os
import logging

logger = logging.getLogger(__name__)


class ServiceRegistry:
    """
    서비스 등록 및 발견을 위한 간단한 클래스
    """

    def __init__(self):
        self.services = {}
        self._load_from_env()

    def _load_from_env(self):
        """환경 변수에서 서비스 URL 로드"""
        service_env_map = {
            "auth": "AUTH_SERVICE_URL",
            "user": "USER_SERVICE_URL",
            "team": "TEAM_SERVICE_URL",
            "project": "PROJECT_SERVICE_URL",
            "notification": "NOTIFICATION_SERVICE_URL"
        }

        for service_name, env_var in service_env_map.items():
            url = os.getenv(env_var)
            if url:
                self.register(service_name, url)
                logger.info(f"Service '{service_name}' registered from environment: {url}")

    def register(self, service_name: str, url: str):
        """서비스 등록"""
        self.services[service_name] = url

    def get_service_url(self, service_name: str) -> Optional[str]:
        """서비스 URL 조회"""
        return self.services.get(service_name)

    def get_all_services(self) -> Dict[str, str]:
        """모든 서비스 URL 반환"""
        return self.services.copy()


# 전역 서비스 레지스트리 인스턴스
service_registry = ServiceRegistry()