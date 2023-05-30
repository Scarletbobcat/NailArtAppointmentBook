import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Scarletbobcat:Gnaoh_2002@nail-art.boejdrj.mongodb.net/")
db = client['Nail-Art']
employees = db['Employee']

post1 = {"_id": 0, "name": "Sami"}
post2 = {"_id": 1, "name": "Brian"}

results1 = employees.find({"_id": 0})
results2 = employees.find({"_id": 1})

for x in results1:
    print(x)
for x in results2:
    print(x)