from utils import *
from menu_controller import *
#URI  = "mongodb://localhost:27017"
#database = "Pachaqtec"

#conn = Conexion(URI,database)

#alumno = Alumno(1,"juan",15,"eljuan@hotmail.com")

#conn.insertar_registro("alumnos",alumno.ToDic())
#conexion = Conexion(URI,database)



#res = conexion.obtener_registros('alumnos')
#print(tabulate([list(i.values()) for i in res],headers=["id","nombre","edad","correo"],tablefmt='fancy_grid'))
#obtener a un alumno

# Define la condición de búsqueda
#condicion = {'nombre': "Jhon"}
#var = conexion.obtener_registro('alumnos',condicion)

# Busca un documento que cumpla con la condición especificada
#print(var)
#print(var2)


try:
    opMenuPrincipal = {"Mostrar Datos": "1", "Crear Datos": "2","Borrar Datos":"3","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            menuSecundario = ""
            opMenuSec = {"Mostrar Alumnos": "1", "Mostrar Salones": "2","Mostrar Cursos": "3","Mostrar Profesores": "4", "Salir": "0"}
            menuSec = Menu("Secundario", opMenuSec)
            ansMenuSec = menuSec.show()
            collection = ""
            if(ansMenuSec == "1"):
                operacionesAlumno("1")
            if(ansMenuSec == "2"):#mostrar salones
                operacionesSalon("1")
            if(ansMenuSec == "3"): #mostrar cursos
                operacionesCurso("1")
            if(ansMenuSec == "4"): #mostrar profesores
                operacionesProfesor("1")
            #print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea continuar??: ")

        if(ansMenuPrincipal == "2"):
            menuSecundario = ""
            opMenuSec = {"Crear Alumnos": "1", "Crear Salones": "2","Crear Cursos": "3","Crear Profesores": "4"}
            menuSec = Menu("Secundario", opMenuSec)
            ansMenuSec = menuSec.show()
            if(ansMenuSec == "1"):
                operacionesAlumno("2")
                print("Datos creados correctamente")
            if(ansMenuSec == "2"):
                operacionesSalon("2")
                print("Datos creados correctamente")
            if(ansMenuSec == "3"):
                operacionesCurso("2")
                print("Datos creados correctamente")
            if(ansMenuSec == "4"):
                operacionesProfesor("2")
                print("Datos creados correctamente")
            
            input("Desea continuar???")

        if(ansMenuPrincipal=="3"):
            menuSecundario = "" 
            opMenuSec = {"Borrar Alumnos": "1", "Borrar Salones": "2","Borrar Cursos": "3","Borrar Profesores": "4"}
            menuSec = Menu("Secundario", opMenuSec)
            ansMenuSec = menuSec.show()

            if(ansMenuSec == "1"):
                operacionesAlumno("3")
                print("Datos eliminados correctamente")
            if(ansMenuSec == "2"):
                operacionesSalon("3")
                print("Datos eliminados correctamente")
            if(ansMenuSec == "3"):
                operacionesCurso("3")
                print("Datos eliminados correctamente")
            if(ansMenuSec == "4"):
                operacionesProfesor("3")
                print("Datos eliminados correctamente")
            input("Desea continuar???")

except Exception as error:
    print(str(error))