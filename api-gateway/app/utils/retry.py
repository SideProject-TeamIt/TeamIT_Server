import asyncio
from typing import TypeVar, Callable, Any, Optional
import logging

T = TypeVar('T')
logger = logging.getLogger(__name__)


async def retry_async(
        func: Callable[..., Any],
        *args: Any,
        retries: int = 3,
        delay: float = 1.0,
        backoff_factor: float = 2.0,
        exceptions: tuple = (Exception,),
        **kwargs: Any
) -> Any:
    """
    비동기 함수에 대한 재시도 로직

    Args:
        func: 재시도할 비동기 함수
        *args: 함수에 전달할 위치 인자
        retries: 최대 재시도 횟수
        delay: 첫 번째 재시도 전 대기 시간(초)
        backoff_factor: 지수 백오프 계수
        exceptions: 캐치할 예외 튜플
        **kwargs: 함수에 전달할 키워드 인자

    Returns:
        함수의 반환값

    Raises:
        마지막 발생한 예외
    """
    last_exception = None
    current_delay = delay

    for attempt in range(retries + 1):
        try:
            return await func(*args, **kwargs)
        except exceptions as e:
            last_exception = e
            if attempt < retries:
                logger.warning(
                    f"Attempt {attempt + 1}/{retries + 1} failed: {str(e)}. "
                    f"Retrying in {current_delay:.2f} seconds..."
                )
                await asyncio.sleep(current_delay)
                current_delay *= backoff_factor
            else:
                logger.error(f"All {retries + 1} attempts failed.")
                raise

    # 여기까지 오면 안되지만, 타입 체크를 위해 추가
    if last_exception:
        raise last_exception
    return None