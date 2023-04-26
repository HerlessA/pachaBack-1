from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')

db = client.Farmacia
collection = db.clientes

data = {
'dni': '99999999', 'nombre': 'Karen', 'apellido': 'Lam', 'direccion': 'Chiclayo'
}

result = collection.insert_one(data)

print(f"Registro insertado {result.inserted_id}")
print(list(collection.find()))


