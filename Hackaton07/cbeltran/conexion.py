from pymongo import MongoClient
from pymongo.server_api import ServerApi

class Conexion:
    def __init__(self, uri, database):
        try:
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client[database]
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")

    def obtener_registros(self, collection, condition={}):
        try:
            collection = self.db[collection]
            data = collection.find(condition)
            return list(data)
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")

    def Close(self):
        try:
            self.db.close()
            print("Esta conexion se ha cerrado correctamente")
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")