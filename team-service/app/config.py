from shared.database.mongodb import mongo_db

# MongoDB 컬렉션 정의
team_collection = mongo_db["teams"]
member_collection = mongo_db["team_members"]