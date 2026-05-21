import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["salon_db"]

appointments_collection = db["appointments"]
users_collection = db["users"]