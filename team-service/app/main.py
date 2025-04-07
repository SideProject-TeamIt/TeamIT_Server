from shared.config.base_config import BaseConfig
from shared.database.mongo import get_mongo_client

mongo_uri = BaseConfig.get_mongo_uri()
client = get_mongo_client(mongo_uri)
db = client[BaseConfig.MONGO_DB]
