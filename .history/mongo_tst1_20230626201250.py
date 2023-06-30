from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://Nton118:gcVS%40_U2Dm%40m8B9@cluster0.lmtksa2.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)

db = client.book

db.cats.update_one({"name": "Barsik"}, {"$set": {"age": 5}})
result = db.cats.find_one({"name": "Barsik"})
print(result)