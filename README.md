Project Title: CRUD Python Module

This project is a Python module designed to perform basic CRUD (Create, Read, Update, Delete) operations on a MongoDB database. The module provides an interface to interact with the database, allowing users to add new records, retrieve existing records, update records, and delete records.

Motivation

The motivation behind this project is to create a simple yet powerful tool for managing data within a database. This module aims to provide an easy-to-use interface for performing CRUD operations, which are fundamental for any data-driven application. By developing this module, I aim to enhance my understanding of database interactions and improve my Python programming skills.

Getting Started

To get a local copy up and running, follow these simple steps:
1.	Clone the repository:
git clone https://github.com/MartLo28/animal_shelter_project/
2.	Navigate to the project directory:
cd animal_shelter_project
3.	Install the required libraries:
pip install -r requirements.txt

Usage

Here are some examples of how the CRUD Python module can be used:
1.	Creating a new record:
from animal_shelter import AnimalShelter

shelter = AnimalShelter("username", "password")
data = {"name": "Fluffy", "species": "Cat"}
shelter.create(data)
2.	Reading existing records:
from animal_shelter import AnimalShelter

shelter = AnimalShelter("username", "password")
records = shelter.read({"species": "Cat"})
for record in records:
    print(record)

Code Example

Tests
Below is an example of the create and read methods in the AnimalShelter class:
import pymongo
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = pymongo.MongoClient(f'mongodb://{username}:{password}@localhost:27017/AAC')
        self.database = self.client['AAC']
        
    # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD.
    def read(self, query):
        return self.database.animals.find(query)

Screenshots


1. **Creating Object:**

   ![Creating Object](images/Screenshot 2024-05-30 225720.png)

