import pymongo
from bson.objectid import ObjectId
from clases import Alumno
from clases import Profesor
from clases import Salon
from clases import Curso
from clases import TemplateObject
from clases import DataBase
from clases import Menu

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIME_FUERA = 1000

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"

Mongo_BASE_DATOS = "SV74090844_Escuela_"


baseData = DataBase(MONGO_URI,MONGO_TIME_FUERA,Mongo_BASE_DATOS)
baseData.createTestValues()


Alumno_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
Profesor_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
Salon_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
Cursos_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
MenuMain_op = {"Menu Alumnos":"1","Menu Profesores":"2","Menu Salones":"3","Menu Cursos":"4","Exit":"0"}



Menu_Alumno = Menu("ALUMNOS",Alumno_op)

Menu_Profesor = Menu("PROFESORES",Profesor_op)

Menu_Salon = Menu("SALONES",Salon_op)

Menu_Cursos = Menu("CURSOS",Cursos_op)

Menu_Main = Menu("MENU PRINCIPAL",MenuMain_op)


f = True
while f:
    ans = Menu_Main.show()

    if(ans == "0"):
        f = False

    if(ans.upper() == "1"):
        respuesta = Menu_Alumno.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")
            edad = input("edad: ")
            correo = input("correo: ")
            notas = input("notas:([15,15,15]): ")

            print("----Salones actuales----") 
            for salon in baseData.collectionSalones.find():
                print("Nombre: " + salon["nombre"] + "      " + "Id_salon: " + str(salon["_id"]))

            salon_id = int(input("Id de salon del alumno: "))
            alumno = Alumno(baseData.collectionAlumnos.count_documents({})+1,nombre, edad,correo,notas,salon_id)
            if(baseData.collectionAlumnos.insert_one(alumno.__dict__)):
                print("Se creo el alumno correctamente")


        elif(respuesta.upper() =="2"):
            id_ = int(input("_id de alumno: "))
            print(baseData.collectionAlumnos.find_one({"_id":id_}))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de alumno para actualizar: "))
            data = baseData.collectionAlumnos.find_one({"_id":id_})
            print(data)

            if(data):

                nombre = input("Nombre: ")
                edad = input("edad: ")
                correo = input("correo: ")
                notas = input("notas:([15,15,15]): ")
                print("----Salones actuales----") 
                for salon in baseData.collectionSalones.find():
                    print("Nombre: " + salon["nombre"] + "      " + "Id_salon: " + str(salon["_id"]))

                salon_id = int(input("Id de salon del alumno: "))

                filtro = {"_id": id_}
                nuevoAlumno =  {"$set": {"nombre": nombre, "edad": edad, "correo":correo, "notas": notas, "id_salon": salon_id}}

                if(baseData.collectionAlumnos.update_one(filtro, nuevoAlumno)):
                    print("Se actualizo correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de alumno para borrar: "))
            filtro = {"_id": id_}
            if(baseData.collectionAlumnos.delete_one(filtro)):
                    print("Se borro correctamente")


        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")

    if(ans.upper() == "2"):
        respuesta = Menu_Alumno.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")
            edad = input("edad: ")
            correo = input("correo: ")

            print("----Salones actuales----") 
            for salon in baseData.collectionSalones.find():
                print("Nombre: " + salon["nombre"] + "      " + "Id_salon: " + str(salon["_id"]))
            salon_id = int(input("Id de salon del profesor: "))

            profesor = Profesor(baseData.collectionProfesores.count_documents({})+1,nombre,edad,correo,salon_id)

            if(baseData.collectionProfesores.insert_one(profesor.__dict__)):
                print("Se creo el profesor correctamente")


        elif(respuesta.upper() =="2"):
            id_ = int(input("Id de profesor: "))
            print(baseData.collectionProfesores.find_one({"_id":id_}))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de profesor para actualizar: "))
            data = baseData.collectionProfesores.find_one({"_id":id_})
            print(data)

            if(data):
                nombre = input("Nombre: ")
                edad = input("edad: ")
                correo = input("correo: ")

                print("----Salones actuales----") 
                for salon in baseData.collectionSalones.find():
                    print("Nombre: " + salon["nombre"] + "      " + "Id_salon: " + str(salon["_id"]))

                salon_id = int(input("Id de salon del profesor: "))

                filtro = {"_id": id_}
                nuevoProfe = Profesor(id_, nombre, edad,correo,salon_id)
                
                if(baseData.collectionProfesores.update_one(filtro,{"$set": nuevoProfe.__dict__})):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de profesor para borrar: "))
            if(baseData.collectionProfesores.delete_one({"_id": id_})):
                    print("Se borro correctamente")


        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")


    if(ans.upper() == "3"):#3333333333
        respuesta = Menu_Salon.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")
            anio = input("Año(yy-mm-dd): ")
            salon = Salon(baseData.collectionSalones.count_documents({})+1, nombre, anio)

            if(baseData.collectionSalones.insert_one(salon.__dict__)):
                print("Se creo el salon correctamente")


        elif(respuesta.upper() =="2"):
            id_salon = int(input("Id de salon: "))
            print(baseData.collectionSalones.find_one({"_id": id_salon}))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de salon para actualizar: "))
            print(baseData.collectionSalones.find_one({"_id": id_}))

            if(baseData.collectionSalones.find_one({"_id": id_})):

                nombre = input("Nombre: ")
                anio = input("Año(yy-mm-dd): ")
                salon = Salon(id_,nombre, anio)
                filtro = {"_id": id_}
                query = {"$set": salon.__dict__}
                if(baseData.collectionSalones.update_one(filtro,query)):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de salon para borrar: "))
            if(baseData.collectionSalones.delete_one({"_id": id_})):
                    print("Se borro correctamente")

        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")


    if(ans.upper() == "4"):
        respuesta = Menu_Cursos.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")

            print("----Profesores actuales----") 
            for prof in baseData.collectionProfesores.find():
                print("Id_profesor: " + prof["_id"] + "         " + "Nombre: " + prof["nombre"])

            profesor_id = int(input("Id de profesor del curso: "))

            curso = Curso(baseData.collectionCursos.count_documents({})+1,nombre,profesor_id)

            if(baseData.collectionCursos.insert_one(curso.__dict__)):
                print("Se creo el curso correctamente")


        elif(respuesta.upper() =="2"):
            id_ = int(input("Id de curso: "))
            print(baseData.collectionCursos.find_one({"_id":id_}))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de curso para actualizar: "))
            print(baseData.collectionCursos.find_one({"_id":id_}))

            if(baseData.collectionCursos.find_one({"_id":id_})):

                nombre = input("Nombre: ")
                print("----Profesores actuales----") 
                for profs in baseData.collectionProfesores.find():
                    print("Nombre profesor: " + profs["nombre"] + "         " + "Id profesor: " + str(profs["_id"]))

                profesor_id = int(input("Id de profesor del curso: "))
                filtro = {"_id": id_}
                nuevoSalon = Curso(id_, nombre, profesor_id)
                query = {"$set": nuevoSalon.__dict__}
                if(baseData.collectionCursos.update_one(filtro, query)):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de curso para borrar: "))
            
            if(baseData.collectionCursos.delete_one({"_id": id_})):
                    print("Se borro correctamente")

        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")

    elif(ans == "0"):
        f = False




