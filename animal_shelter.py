import os
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        username = 'accuser' #os.getenv('MONGO_USER')
        password = 'pwd123' #os.getenv('MONGO_PASS')
        host = os.getenv('MONGO_HOST', 'localhost')
        port = int(os.getenv('MONGO_PORT', 27017))
        db_name = os.getenv('MONGO_DB', 'AAC')
        col_name = os.getenv('MONGO_COLLECTION', 'animals')

        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db_name]
        self.collection = self.database[col_name]

    def create(self, data):
        """ Method to insert a document into the MongoDB collection """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, query):
        """ Method to query documents from the MongoDB collection """
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"An error occurred: {e}")
                return []
        else:
            raise ValueError("Query parameter is empty")
