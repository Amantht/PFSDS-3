import pymongo
from pymongo import MongoClient
client=pymongo.MongoClient('mongodb://127.0.0.1:27017')
db=client['S3']
employeedata=db.employee
data={"age":20,"name":"def","status":"single"}
data1={"Gender":"male"}
employeedata.insert_one(data)
employeedata.insert_one(data1)
employeedata.find()
data2={"age":"20"}
employeedata.delete_one(data2)
old = {"name": "Aman"}
new= {"$set": {"name": "Abc"}}
employeedata.update_one(old, new)
data1={"Gender":"male"}
employeedata.insert_one(data1)
