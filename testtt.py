from pymongo import MongoClient
# create  an instance (DB connectivity)
client=MongoClient('mongodb://127.0.0.1:27017')

# create DB
db=client['Nepal']
test=db.City
data={"capital":"Kathmandu"}
test.insert_one(data)