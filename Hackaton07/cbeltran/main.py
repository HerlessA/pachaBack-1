import src
from src.utils import Menu



opMenuPrincipal = {"Menú Alumnos": "1", "Menú Profesores": "2","Menú Salón": "3","Menú Crusos":"4","Salir": "0"}
showHome = True
ansMenuPrincipal = ""
menuPrincipal = Menu("Principal", opMenuPrincipal)

while showHome:
    ansMenuPrincipal = menuPrincipal.show()
    if(ansMenuPrincipal == "0"):
        break

    if(ansMenuPrincipal == "1"):
                opMenuAlumnos = {"Listar Alumnos": "1", "Crear Alumno": "2","Editar Alumno": "3","Eliminar Alumno":"4","Salir": "0"}
                ansAlumnos = ""
                menuAlumnos = Menu("Alumnos", opMenuAlumnos)
                ansAlumnos = menuAlumnos.show()
                if (ansAlumnos == "1"):
                    
                    print(src.clsAlumno.listar_alumnos())

