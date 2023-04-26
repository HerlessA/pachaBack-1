import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["SV70098291"]
mycol = mydb["Alumno"]

def listar_alumnos():
    try:
            for x in mycol.find():
                return print(x)
    except Exception as error:
            print(f"Ha ocurrido un error: {error}")
