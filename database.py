from pymongo import MongoClient
import config 

client = MongoClient(config.MONGO_URI)

db = client[config.DATABASE_NAME]

collection = db[config.COLLECTION_NAME]