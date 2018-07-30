import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "anniestestdb"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# Let's insert more records by using an array to send in multiple dictionaries! 

new_docs = [{'first': 'terry', 'last': 'pratchett', 'hair_colour': 'not much', 'gender': 'm', 'occupation': 'writer', 'nationality': 'english'},
            {'first': 'annie', 'last': 'johnston', 'hair_colour': 'brown', 'gender': 'm', 'occupation': 'admin', 'nationality': 'german'}]

coll.insert_many(new_docs)
""" very import: insert_many  !!!"""

documents = coll.find()

for doc in documents:
    print(doc)