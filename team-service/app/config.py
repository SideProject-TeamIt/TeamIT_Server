from shared.database.mongo import get_mongo_client
from shared.config.base_config import BaseConfig

# MongoDB 클라이언트 및 DB 초기화
mongo_uri = BaseConfig.get_mongo_uri()
client = get_mongo_client(mongo_uri)
db = client[BaseConfig.MONGO_DB]

# MongoDB 컬렉션 정의
team_collection = db["teams"]
member_collection = db["team_members"]