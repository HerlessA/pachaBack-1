from conexion import Conexion
from utils import Menu
from clases import Alumnos
from clases import Profesores
from clases import Persona
from clases import Salones
from clases import Cursos
from tabulate import TableFormat, tabulate

lstAlumnos = []
lstSalones = []
lstCursos = []
lstProfesores = []

condicion = {
    'Con': '1'
}

def cargaAlumnos():
    res = Conexion.obtener_registros("Alumnos",condicion)
    for alu in res:
        alumno = Alumnos(alu[0], alu[1], alu[2], alu[3], alu[4], alu[5])
        lstAlumnos.append(alumno)
cargaAlumnos()
def cargaSalones():
    res = Conexion.obtener_registros("Salones", condicion)
    for sal in res:
        salon = Salones(sal[0], sal[1])
        lstSalones.append(salon)
cargaSalones()
def cargaCursos():
    res = Conexion.obtener_registros("Cursos",condicion)
    for cur in res:
        curso = Cursos(cur[0], cur[1])
        lstCursos.append(curso)
cargaCursos()
def cargaProfesores():
    res = Conexion.obtener_registros("Profesores",condicion)
    for pro in res:
        profesor = Profesores(pro[0], pro[1], pro[2], pro[3], pro[4])
        lstProfesores.append(profesor)
cargaProfesores()
try:
    opMenuPrincipal = {"Mostrar Alumnos": "1", "Editar Alumnos": "2","Crear Alumno": "3","Borrar Alumno":"4", "Mostrar Profesores": "5", "Editar Profesor": "6","Crear Profesor": "7","Borrar Profesor":"8", "Mostrar Cursos": "9", "Editar Curso": "10","Crear Curso": "11","Borrar Curso":"12","Mostrar Salones": "13", "Editar Salon": "14","Crear Salon": "15","Borrar Salon":"16","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            header = ['ID','Nombre','Edad','Correo','Salon', 'Notas']
            res = Conexion.obtener_registros("Alumnos",condicion)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "2"):
            IdAlumno = int(input("Que alumno deseas editar: "))
            condicion1 = {"Id" : IdAlumno}
            res = Conexion.obtener_registro("Alumnos",condicion1)
            header = ['ID','Nombre','Edad','Correo','Salon', 'Notas']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            nota = int(input("Dime tu nota: "))
            newValues = {"$set": {"nombre":nombre, "edad": edad, "correo": correo, "salon" : salon, "nota" = nota}}
            if(Conexion.actualizar_registro("Alumnos",condicion1,newValues)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="3"):
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            nota = int(input("Dime tu nota: "))
            newValues = {"$set": {"nombre":nombre} {"edad": edad} {"correo": correo} {"salon" : salon} {"nota" = nota}}
            if(Conexion.insertar_registro("Alumnos",newValues)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "4"):
            IdAlumno = int(input("Que alumno deseas borrar: "))
            condicion1 = {"Id" : IdAlumno}
            res = Conexion.obtener_registro("Alumnos",condicion1)
            header = ['ID','Nombre','Edad','Correo','Salon', 'Notas']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            if(Conexion.borrar_registro("Alumnos",condicion1)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "5"):
            header = ['ID','Nombre','Edad','Correo','Salon']
            res = Conexion.obtener_registros("Profesores",condicion)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "6"):
            IdProfesor = int(input("Que profesor deseas editar: "))
            condicion2 = {"Id" : IdProfesor}
            res = Conexion.obtener_registro("Profesores",condicion2)
            header = ['ID','Nombre','Edad','Correo','Salon']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            newValues = {"$set": {"nombre":nombre} {"edad": edad} {"correo": correo} {"salon" : salon}}
            if(Conexion.actualizar_registro("Profesores",condicion2)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="7"):
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            newValues = {"$set": {"nombre":nombre} {"edad": edad} {"correo": correo} {"salon" : salon}}
            if(Conexion.insertar_registro("Profesores",newValues)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "8"):
            IdProfesor = int(input("Que profesor deseas borrar: "))
            condicion2 = {"Id" : IdProfesor}
            res = Conexion.obtener_registro("Profesores",condicion2)
            header = ['ID','Nombre','Edad','Correo','Salon']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            if(Conexion.borrar_registro("Profesores",condicion2)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "9"):
            header = ['Nombre','Profesor']
            res = Conexion.obtener_registros("Cursos")
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "10"):
            Nombre = int(input("Que curso deseas editar: "))
            condicion3 = {"Nombre" : Nombre}
            res = Conexion.obtener_registro("Cursos",condicion3)
            header = ['Nombre','Profesor']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            profesor = input("Dime tu profesor: ")
            newValues = {"$set": {"Profesor":profesor}}
            if(Conexion.actualizar_registro("Cursos",condicion3,newValues)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="11"):
            profesor = input("Dime tu profesor: ")
            newValues = {"$set": {"Profesor":profesor}}
            if(Conexion.insertar_registro("Cursos",newValues)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "12"):
            Nombre = int(input("Que curso deseas borrar: "))
            condicion3 = {"Nombre" : Nombre}
            res = Conexion.obtener_registro("Cursos",condicion3)
            header = ['Nombre','Profesor']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            if(Conexion.borrar_registro("Cursos",condicion3)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "13"):
            header = ['Nombre','Año escolar']
            res = Conexion.obtener_registros("Salones",condicion)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "14"):
            Nombre = int(input("Que salon deseas editar: "))
            condicion3 = {"Nombre" : Nombre}
            res = Conexion.obtener_registros("Salones",condicion3)
            header = ['Nombre','Año']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            anho = input("Dime tu año escolar: ")
            newValues = {"$set": {"Año":anho}}
            if(Conexion.actualizar_registro("Salones",condicion3,newValues)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="15"):
            anho = input("Dime tu año escolar: ")
            newValues = {"$set": {"Año":anho}}
            if(Conexion.insertar_registro("Salones",newValues)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "16"):
            Nombre = int(input("Que salon deseas borrar: "))
            condicion3 = {"Nombre" : Nombre}
            res = Conexion.borrar_registro("Salones",condicion3)
            header = ['Nombre','Año escolar']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            if(Conexion.borrar_registro("Salones",condicion3)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))