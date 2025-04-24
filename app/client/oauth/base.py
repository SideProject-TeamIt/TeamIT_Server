from abc import ABC, abstractmethod
from fastapi import Request
from starlette.responses import RedirectResponse, Response

class OAuthClient(ABC):
    @abstractmethod
    async def get_redirect_url(self) -> RedirectResponse:
        ...

    @abstractmethod
    async def process_callback(self, request: Request) -> dict:
        ...
