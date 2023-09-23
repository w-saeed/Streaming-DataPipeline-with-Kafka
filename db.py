from pymongo import MongoClient

try:
    conn = MongoClient('localhost', 27017)
    print("Connected successfully!!!")
except:
    print("Error while connecting to MongoDB")

# database connection
db = conn.database

# Created a collection names Streaming_data
collection = db.Streaming_data


def save(message):
    save = collection.insert_one(message)
