from pymongo import MongoClient
# create  an instance (DB connectivity)
client=MongoClient('mongodb://127.0.0.1:27017')

# create DB
db=client['s3']

# create collection
studentdata=db.students

# create Documents
  # create single Document
Student1={"regd":"111","name":"abc"}
  # create multiple Documents
Student2=[{"regd":"222","name":"def"},{"regd":"333","name":"abc"},{"regd":"444","name":"ghi"}]

# Insert Document
  # Insert one Document
studentdata.insert_one(Student1)
  # Insert many Document
studentdata.insert_many(Student2)

# retrieve Documents
  # retrieve one Documents
studentdata.find_one(Student1)

# retrive multiple
a={"name":"abc"}
for x in studentdata.find(a):
    print(x)

# delete document
# delete single document
b={"redg":"222"}
studentdata.delete_one(b)

# delete multiple
c={"name":"abc"}
studentdata.delete_many(c)

# update
old = {"name": "Aman"}
new= {"$set": {"name": "Can"}}
studentdata.update_one(old, new)