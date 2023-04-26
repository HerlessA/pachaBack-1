from pymongo import MongoClient, errors

class conexion:
    def __init__(self, uri, database):
        self.client = MongoClient(uri)
        self.db = self.client[database]

    def insertar_registro(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)
        print(f'Registro insertado: {result.inserted_id}')

    def obtener_registros(self, collection, condition={}):
        collection = self.db[collection]
        data = collection.find(condition)
        return list(data)

    def obtener_registro(self, collection, condition = {}):
        collection = self.db[collection]
        data = collection.find_one(condition)
        return data
    
    def actualizar_registro(self, collection, filter={}, change = {}):
        try:
            collection = self.db[collection]
            newValues = { "$set":change}
            collection.update_one(filter, newValues)
            print('Registro actualizado')
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
    
    def cerrar_conexion(self):
        self.db.close()
        print("Se cerró la conexión")
        return True
