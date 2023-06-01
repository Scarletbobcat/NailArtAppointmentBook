import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

#finds .env file
load_dotenv(find_dotenv())

#assigns password from .env file
password = os.environ.get("MONGO_PWD")

connection_string = f"mongodb+srv://Scarletbobcat:{password}@nail-art.boejdrj.mongodb.net/"

#connecting to database and collections
client = MongoClient(connection_string)
db = client['Nail-Art']
employees = db.Employee
appointments = db.Appointments

#docs are all employees
current_employees =[
{"_id": 0, "name": "Sami"},
{"_id": 1, "name": "Brian"},
{"_id": 2, "name": "Ken"},
{"_id": 3, "name": "Ty"},
{"_id": 4, "name": "Rachel"},
{"_id": 5, "name": "Rae"},
{"_id": 6, "name": "Tien"},
{"_id": 7, "name": "Taylor"}]

#to insert all current employees
# for x in current_employees:
#     if (employees.find_one(x)):
#         print(x.name + " is already an employee!\n")
#     else:
#         employees.insert_one(x)

#finding documents with specific id
# results1 = employees.find({"_id": 0})

#menu function that prints menu
def menu():
    print("1. Create appointment\n2. Delete appointment\n3. Add nail tech\n4. Remove nail tech\n5. Exit\n")

while True:
    menu()
    choice = input()

    match choice:
        case "1":
            #ask date, name, start time, end time, phone number, service,
            date = input("Date: ")
            name = input("Name: ")
            start_time = input("Start time: ")
            end_time = input("End time: ")
            phone_number = input("Phone number: ")
            service = input("Service: ")
            nail_technician = input("Nail Tech: ")
            #if appointment exists
            if appointments.find_one({"date": date, "name": name, "start_time": start_time}):
                #print appointment already exists
                print("Appointment already exists")
            #else
            else:
                #add appointment to database
                post = {"date": date, "name": name, "start_time": start_time, "end_time": end_time, "phone_number": phone_number, "service": service}
                appointments.insert_one(post)

        case "2":
            #ask date, name, time
            date = input("Date: ")
            name = input("Name: ")
            start_time = input("Start time: ")
            #if appointment does not exist
            if not appointments.find_one({"date": date, "name": name, "start_time": start_time}):
                #print appointment does not exist
                print("Appointment does not exist")
            while appointments.find_one({"date": date, "name": name, "start_time": start_time}):
                #remove from database
                appointments.delete_one({"date": date, "name": name, "start_time": start_time})

        case "3":
            #ask who to add
            nail_tech = input("First name of nail tech: ")
            #if nail tech exists
            if employees.find_one({"name": nail_tech}):
                #print nail tech already exists
                print("Employee already exists")
            #else if nail tech does not exist
            else:
                #add nail tech to database
                employees.insert_one({"name": nail_tech})

        case "4":
            #ask who to remove
            nail_tech = input("First name of nail tech: ")
            #if name exists
            if employees.find_one({"name": nail_tech}):
                #remove nail tech
                employees.delete_one({"name": nail_tech})
            #else print DNE
            else:
                print("Nail tech does not exist")

        case "5":
            #close program
            break