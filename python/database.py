import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

#finds .env file
load_dotenv(find_dotenv())

#assigns password from .env file
password = os.environ.get("MONGO_PWD")

#connecting to database and collections
client = MongoClient(f"mongodb+srv://Scarletbobcat:{password}@nail-art.boejdrj.mongodb.net/")
db = client['Nail-Art']
employees = db['Employee']

#posts to create documents
post1 = {"_id": 0, "name": "Sami"}
post2 = {"_id": 1, "name": "Brian"}

#finding documents with specific id
results1 = employees.find({"_id": 0})
results2 = employees.find({"_id": 1})

#printing all information related to these documents
for x in results1:
    print(x)
for x in results2:
    print(x)