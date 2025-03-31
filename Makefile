COMPOSE = docker-compose

# 전체 서비스 빌드
build:
	$(COMPOSE) build

# 전체 서비스 실행 (백그라운드)
up:
	$(COMPOSE) up -d

# 전체 서비스 중지 및 컨테이너 제거
down:
	$(COMPOSE) down

# 로그 실시간 출력
logs:
	$(COMPOSE) logs -f

# 특정 서비스 재시작
restart-auth:
	$(COMPOSE) restart auth-service

restart-user:
	$(COMPOSE) restart user-service

restart-team:
	$(COMPOSE) restart team-service

restart-project:
	$(COMPOSE) restart project-service

restart-notification:
	$(COMPOSE) restart notification-service

restart-gateway:
	$(COMPOSE) restart api-gateway

# 전체 재시작
restart-all:
	$(MAKE) restart-auth
	$(MAKE) restart-user
	$(MAKE) restart-team
	$(MAKE) restart-project
	$(MAKE) restart-notification
	$(MAKE) restart-gateway

# 테스트 실행 (예: pytest 사용 시, 테스트 디렉토리에서)
test-auth:
	$(COMPOSE) run --rm auth-service pytest tests/auth-service

test-user:
	$(COMPOSE) run --rm user-service pytest tests/user-service

test-team:
	$(COMPOSE) run --rm team-service pytest tests/team-service

test-project:
	$(COMPOSE) run --rm project-service pytest tests/project-service

test-notification:
	$(COMPOSE) run --rm notification-service pytest tests/notification-service

# 전체 테스트 실행
test-all:
	$(MAKE) test-auth
	$(MAKE) test-user
	$(MAKE) test-team
	$(MAKE) test-project
	$(MAKE) test-notification
