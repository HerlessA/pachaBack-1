#opciones para alumnos
from conexion import Conexion
from models import *
from tabulate import tabulate
URI  = "mongodb://localhost:27017"
database = "Pachaqtec"
conexion = Conexion(URI,database)
# "1"-> obtener registros
# "2"-> crear registros
# "3"-> modificar registros
# "4"->eliminar registros
#
def operacionesAlumno(opcion):
    if opcion == "1": #obtener registro
        res = conexion.obtener_registros('alumnos')
        print(tabulate([list(i.values()) for i in res],headers=["id","nombre","edad","correo"],tablefmt='fancy_grid'))
        
    elif opcion == "2": #insertar nuevo dato
        name = input("ingrese el nombre de alumno: ")
        edad = int(input("ingrese la edad del alumno: "))
        correo = input("ingrese el correo del alumno: ")
        al = Alumno(name,edad,correo)
        conexion.insertar_registro('alumnos',al.ToDic())
    elif opcion == "3": 
        att=input("elija el nombre del alumno a eliminar: ")
        condicion = {'nombre':att}
        conexion.borrar_registro('alumnos',condicion)
        
def operacionesCurso(opcion):
    if opcion == "1": #obtener registro
        res = conexion.obtener_registros('cursos')
        print(tabulate([list(i.values()) for i in res],headers=["id","nombre del curso","profesor asignado"],tablefmt='fancy_grid'))
        
    elif opcion == "2": #insertar nuevo dato
        name = input("ingrese el nombre del curso: ")
        profesor_asignado = input("ingrese el nombre del profesor asignado: ")
        curso = Curso(name,profesor_asignado)
        conexion.insertar_registro('cursos',curso.ToDic())
    elif opcion == "3": 
        att=input("elija el nombre del curso a eliminar: ")
        condicion = {'nombre del curso':att}
        conexion.borrar_registro('cursos',condicion)

def operacionesProfesor(opcion):
    if opcion == "1": #obtener registro
        res = conexion.obtener_registros('profesores')
        print(tabulate([list(i.values()) for i in res],headers=["id","nombre","edad","correo"],tablefmt='fancy_grid'))
        
    elif opcion == "2": #insertar nuevo dato
        name = input("ingrese el nombre de profesor: ")
        edad = int(input("ingrese la edad del profesor: "))
        correo = input("ingrese el correo del profesor: ")
        profe = Profesor(name,edad,correo)
        conexion.insertar_registro('profesores',profe.ToDic())
    elif opcion == "3": 
        att=input("elija el nombre del profesor a eliminar: ")
        condicion = {'nombre':att}
        conexion.borrar_registro('profesores',condicion)

def operacionesSalon(opcion):
    if opcion == "1": #obtener registro
        res = conexion.obtener_registros('salones')
        print(tabulate([list(i.values()) for i in res],headers=["id","nombre","año escolar"],tablefmt='fancy_grid'))
        
    elif opcion == "2": #insertar nuevo dato
        name = input("ingrese el nombre del salon: ")
        anio = input("ingrese el año escolar del salón: ")
        salon = Salon(name,anio)
        conexion.insertar_registro('salones',salon.ToDic())
    elif opcion == "3": 
        att=input("elija el nombre del salon a eliminar: ")
        condicion = {'nombre del salon':att}
        conexion.borrar_registro('salones',condicion)