from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['uk_food']
with open('establishments.json', encoding='utf-8') as file:
    data = json.load(file)
collection = db['establishments']
collection.insert_many(data)
client.close()
