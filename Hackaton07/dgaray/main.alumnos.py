from utils import Menu
from conexion import Conexion
from tabulate import TableFormat, tabulate
from bson.objectid import ObjectId

conn = Conexion("mongodb://localhost:27017", "Colegio")


class Alumno:
    def __init__(self, nombreAlumno, email, edad, curso, salon):
        self.nombreAlumno = nombreAlumno
        self.email = email
        self.edad = edad
        self.curso = curso
        self.salon = salon

    def ToDic(self):
        return {
            "nombre": self.nombreAlumno,
            "email": self.email,
            "edad": self.edad,
            "curso": self.curso,
            "salon": self.salon,
        }


try:
    opMenuPrincipal = {
        "Mostrar Alumnos": "1",
        "Editar Alumno": "2",
        "Crear Alumno": "3",
        "Borrar Alumno": "4",
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
            res = conn.obtener_registros("alumnos")
            print(res)
            input("Desea contunuar??")

        if ansMenuPrincipal == "2":
            idAlumno = input("Que alumno deseas editar: ")
            id_buscado = ObjectId(idAlumno)
            res = conn.obtener_registro("alumnos", id_buscado)
            # header = ["ID", "Nombre", "email", "edad"]
            # print(tabulate(res, headers=header, tablefmt="fancy_grid"))
            print(res)
            input("Desea contunuar??")
            nombreAlumno = input("Dime el nombre del alumno: ")
            print(nombreAlumno)
            email = input("Dime tu email: ")
            edad = int(input("Dime tu edad: "))
            curso = input("Dime el curso: ")
            salon = input("Dime el salon: ")
            
            newvalues = {
                "$set": {
                    "nombre": nombreAlumno,
                    "email": email,
                    "edad": edad,
                    "curso": curso,
                    "salon": salon,
                }
            }
            print(newvalues)
            respuesta = conn.actualizar_registros("alumnos", id_buscado, newvalues)
            if respuesta:
                print("Datos actualizados correctamente")
                input("Desea continuar???")

        if ansMenuPrincipal == "3":
            nombreAlumno = input("Dime el nombre del alumno: ")
            email = input("Dime tu email: ")
            edad = int(input("Dime tu edad: "))
            curso = input("Dime el curso: ")
            salon = input("Dime el salon: ")
            alumno = Alumno(nombreAlumno, email, edad, curso, salon)
            conn.insertar_registro("alumnos", alumno.ToDic())
            if conn:
                print("Datos creados correctamente")
                input("Desea continuar???")

        if ansMenuPrincipal == "4":
            idAlumno = input("Que alumno deseas aliminar: ")
            id_buscado = ObjectId(idAlumno)
            res = conn.obtener_registro("alumnos", id_buscado)
            print(res)
            input("Desea contunuar??")
            respuesta = conn.borrar_registro("alumnos",id_buscado)
            if respuesta:
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))
