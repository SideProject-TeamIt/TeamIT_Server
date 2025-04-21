import logging
import json
import sys
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "service": getattr(record, "service", "unknown"),
            "trace_id": getattr(record, "trace_id", ""),
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)


def setup_logging(service_name, log_level=logging.INFO):
    """
    서비스에 대한 로깅 설정
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    # 루트 로거 설정
    logging.root.handlers = []
    logging.root.addHandler(handler)
    logging.root.setLevel(log_level)

    # 커스텀 로거 설정
    logger = logging.getLogger(service_name)
    logger.setLevel(log_level)

    # 라이브러리 로깅 레벨 조정
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    return logger