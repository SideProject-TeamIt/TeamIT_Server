```
fastapi-msa-monorepo/
├── api-gateway/ (서비스 라우팅, 인증 등 공통 진입점)
│   └── app/
│       ├── main.py
│       ├── config.py
│       └── routers/gateway_router.py
│
├── services/ (각 독립 마이크로서비스 모음)
│   ├── auth-service/ (인증)
│   ├── user-service/ (사용자 프로필 관리)
│   ├── team-service/ (팀 관리)
│   ├── project-service/ (프로젝트 관리)
│   └── notification-service/ (알림)
│
│   → 각 서비스는 동일 구조로 구성:
│     - `main.py` (진입점)
│     - `config.py` (환경설정)
│     - `routers/` (API 엔드포인트)
│     - `services/` (비즈니스 로직)
│     - `models/` (DB 모델)
│     - `schemas/` (API 스키마)
│
├── shared/ (공통 유틸, 예외처리, DB 연결)
├── tests/ (서비스별 테스트 코드)
├── docker-compose.yml (서비스 관리)
├── Makefile (명령어 관리)
└── README.md (프로젝트 문서)
```