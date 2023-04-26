from utils import Menu
from conexion import Conexion
from tabulate import TableFormat, tabulate
from bson.objectid import ObjectId

conn = Conexion("mongodb://localhost:27017", "Colegio")


class Profesor:
    def __init__(self, nombreProfesor, email, edad, curso, salon):
        self.nombreProfesor = nombreProfesor
        self.email = email
        self.edad = edad
        self.curso = curso
        self.salon = salon

    def ToDic(self):
        return {
            "nombre": self.nombreProfesor,
            "email": self.email,
            "edad": self.edad,
            "curso": self.curso,
            "salon": self.salon,
        }


try:
    opMenuPrincipal = {
        "Mostrar Profesores": "1",
        "Editar Profesor": "2",
        "Crear Profesor": "3",
        "Borrar Profesor": "4",
        "Salir": "0",
    }
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if ansMenuPrincipal == "0":
            break
        if ansMenuPrincipal == "1":
            res = conn.obtener_registros("profesores")
            print(res)
            input("Desea contunuar??")

        if ansMenuPrincipal == "2":
            idProfesor = input("Que profesor deseas editar: ")
            id_buscado = ObjectId(idProfesor)
            res = conn.obtener_registro("profesores", id_buscado)
            input("Desea contunuar??")
            nombreProfesor = input("Dime el nombre del profesor: ")
            email = input("Dime tu email: ")
            edad = int(input("Dime tu edad: "))
            curso = input("Dime el curso: ")
            salon = input("Dime el salon: ")
            
            newvalues = {
                "$set": {
                    "nombre": nombreProfesor,
                    "email": email,
                    "edad": edad,
                    "curso": curso,
                    "salon": salon,
                }
            }
            print(newvalues)
            respuesta = conn.actualizar_registros("profesores", id_buscado, newvalues)
            if respuesta:
                print("Datos actualizados correctamente")
                input("Desea continuar???")

        if ansMenuPrincipal == "3":
            nombreAlumno = input("Dime el nombre del alumno: ")
            email = input("Dime tu email: ")
            edad = int(input("Dime tu edad: "))
            curso = input("Dime el curso: ")
            salon = input("Dime el salon: ")
            alumno = Profesor(nombreAlumno, email, edad, curso, salon)
            conn.insertar_registro("profesores", alumno.ToDic())
            if conn:
                print("Datos creados correctamente")
                input("Desea continuar???")

        if ansMenuPrincipal == "4":
            idProfesor = input("Que profesor deseas aliminar: ")
            id_buscado = ObjectId(idProfesor)
            res = conn.obtener_registro("profesores", id_buscado)
            print(res)
            input("Desea contunuar??")
            respuesta = conn.borrar_registro("profesores",id_buscado)
            if respuesta:
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))
