from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.Farmacia
collection = db.enfermeros

# print(list(collection.find()))


collection = db.clientes
data = {
    "dni": "70859641",
    "nombre": "Karen",
    "apellido": "Ugarte",
    "direccion": "Jr. Solar 1237",
}

result = collection.insert_one(data)
print(f"Registr insertado {result.inserted_id}")
print(list(collection.find()))
