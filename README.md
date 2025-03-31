@ -0,0 +1,29 @@
```
TeamIT_Server/
├── api-gateway/ (서비스 라우팅, 인증 등 공통 진입점)
│   └── app/
│       ├── main.py
│       ├── config.py
│       └── routers/gateway_router.py
│   └── Dockerfile
│   └── requirements.txt
│
├── auth-service/ (인증)
├── user-service/ (사용자 프로필 관리)
├── team-service/ (팀 관리)
├── project-service/ (프로젝트 관리)
└── notification-service/ (알림)
│
│ → 각 서비스는 동일 구조로 구성:
│   - `app/main.py` (진입점)
│   - `app/config.py` (환경설정)
│   - `app/routers/` (API 엔드포인트)
│   - `app/services/` (비즈니스 로직)
│   - `app/models/` (DB 모델)
│   - `app/schemas/` (API 스키마)
│   - `Dockerfile` (도커 이미지 빌드)
│   - `requirements.txt` (의존성 관리)
│
├── shared/ (공통 유틸, 예외처리, DB 연결)
├── tests/ (서비스별 테스트 코드)
├── docker-compose.yml (서비스 관리)
├── Makefile (명령어 관리)
└── README.md (프로젝트 문서)
```


## Docker 실행 명령어

### 전체 테스트 
```bash
docker compose up --build
```

### 개별 서비스 테스트
```bash
docker compose up --build <서비스명>
```

### 운영 서버 실행
```bash
docker compose -f docker-compose.yml up
```