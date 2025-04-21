-- 데이터베이스 생성
CREATE DATABASE auth_db;
CREATE DATABASE user_db;

-- 각 DB에 대한 권한 설정
GRANT ALL PRIVILEGES ON DATABASE auth_db TO teamit_user;
GRANT ALL PRIVILEGES ON DATABASE user_db TO teamit_user;