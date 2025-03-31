COMPOSE = docker-compose

# 빌드 및 실행
build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f

# 재시작
restart-%:
	$(COMPOSE) restart $*

# 서비스별 테스트 (pytest 사용 시)
test-%:
	$(COMPOSE) run --rm $*-service pytest tests/

# 전체 테스트 실행
test-all: test-auth test-user test-team test-project test-notification

.PHONY: build up down logs test-all
