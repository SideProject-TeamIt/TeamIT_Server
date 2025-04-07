from pymongo import MongoClient

def get_mongo_client(mongo_uri: str):
    return MongoClient(mongo_uri)
