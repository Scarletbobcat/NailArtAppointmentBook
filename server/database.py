from pymongo import MongoClient
import os
from typing import Union
from fastapi import FastApi
from dotenv import load_dotenv, find_dotenv

app = FastApi()

#finds and loads .env file
load_dotenv(find_dotenv())

#assigns username and password from .env file
username = os.environ.get("MONGO_USRNM")
password = os.environ.get("MONGO_PWD")

connection_string = f"mongodb+srv://{username}:{password}@nail-art.boejdrj.mongodb.net/"

#connecting to database and collections
client = MongoClient(connection_string)
db = client['Nail-Art']
employees = db.Employee
appointments = db.Appointments

next_id = employees.find().count()

#menu function that prints menu
def menu():
    print("\n\n1. Create appointment\n2. Delete appointment\n3. Add nail tech\n4. Remove nail tech\n5. Exit\n")

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
                appointments.insert_one({"date": date, "name": name, "start_time": start_time, "end_time": end_time, "phone_number": phone_number, "service": service})

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
                employees.insert_one({"_id": next_id, "name": nail_tech})
                next_id += 1

        case "4":
            #ask who to remove
            nail_tech = input("First name of nail tech: ")
            #if name exists
            if employees.find_one({"_id": next_id - 1, "name": nail_tech}):
                #remove nail tech
                employees.delete_one({"_id": next_id - 1, "name": nail_tech})
            #else print DNE
            else:
                print("Nail tech does not exist")

        case "5":
            #close program
            break