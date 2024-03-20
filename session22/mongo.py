from os import system
from pymongo import MongoClient
from colorama import Fore, Back,Style

def clear():
    system("cls || clear")

client = MongoClient('localhost', 27017)

db = client.rptutorials

tutorial = db.tutorial

tutorial1 = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": ["Aldren", "Dan", "Joanna"],
    "url": "https://realpython.com/python-json/",
}

resultado = tutorial.insert_one(tutorial1)
print("ID tutorial1", resultado.inserted_id)

tutorial2 = {
    "title": "Python’s Requests Library (Guide)",
    "author": "Alex",
    "contributors": ["Aldren", "Brad", "Joanna"],
    "url": "https://realpython.com/python-requests/",
}

tutorial3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": ["Aldren", "Joanna", "Jacob"],
    "url": "https://realpython.com/python3-object-oriented-programming/",
}


resultado = tutorial.insert_many([tutorial2, tutorial3])
print(resultado.inserted_ids)


for doc in tutorial.find():
    print(doc)
print("-"*100)
alex_doc = tutorial.find_one({"author": "Alex"})
print(alex_doc)

