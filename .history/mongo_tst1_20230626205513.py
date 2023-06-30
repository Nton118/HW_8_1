from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://Nton118:Ttomb95V641aQgZA@cluster0.lmtksa2.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)

db = client.book

db.cats.update_one({"name": "Barsik"}, {"$set": {"age": 5}})
result = db.cats.find_one({"name": "Barsik"})
print(result)
