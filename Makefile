# TeamIT 서버 Makefile

.PHONY: help build-base build-all dev prod start stop restart clean test

# 기본 명령어는 도움말 표시
help:
	@echo "TeamIT 서버 관리 명령어:"
	@echo ""
	@echo "  build-base     - 베이스 도커 이미지 빌드"
	@echo "  build-all      - 모든 서비스 빌드 (베이스 이미지 포함)"
	@echo "  dev            - 개발 환경 실행 (핫 리로드 활성화)"
	@echo "  prod           - 프로덕션 환경 실행"
	@echo "  start          - 모든 서비스 시작"
	@echo "  stop           - 모든 서비스 중지"
	@echo "  restart        - 모든 서비스 재시작"
	@echo "  clean          - 컨테이너, 이미지, 볼륨 삭제"
	@echo "  test           - 모든 테스트 실행"
	@echo ""

# 베이스 이미지 빌드
build-base:
	@echo "Building base image..."
	@docker build -t teamit/base:latest -f docker/base/Dockerfile .
	@echo "Base image built successfully."

# 모든 서비스 빌드
build-all: build-base
	@echo "Building all services..."
	@docker-compose build

# 개발 환경 실행
dev: build-base
	@echo "Starting development environment..."
	@docker-compose up -d
	@echo "Services are running in development mode."
	@echo "API Gateway is available at: http://localhost:8000"

# 프로덕션 환경 실행
prod: build-base
	@echo "Starting production environment..."
	@docker-compose -f docker-compose.yml up -d
	@echo "Services are running in production mode."
	@echo "API Gateway is available at: http://localhost:8000"

# 모든 서비스 시작
start:
	@echo "Starting all services..."
	@docker-compose start

# 모든 서비스 중지
stop:
	@echo "Stopping all services..."
	@docker-compose stop

# 모든 서비스 재시작
restart: stop start
	@echo "All services restarted."

# 컨테이너, 이미지, 볼륨 삭제
clean:
	@echo "Cleaning up containers, images, and volumes..."
	@docker-compose down -v
	@docker rmi teamit/base:latest || true
	@echo "Cleanup completed."

# 모든 테스트 실행
test:
	@echo "Running all tests..."
	@docker-compose run --rm auth-service pytest