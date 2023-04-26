from utils import Menu
from Alumno import Alumno
from AlumnoBD import AlumnoBD
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()
listAlumnos = []

# def obtenerListaAlumnos():
#     query = "select * from alumnos;"
#     resultado = conexion.consultarBDD(query=query)

#     for alumn in resultado:
#         alumno = Alumno(alumn[0], alumn[1], alumn[2], alumn[3], alumn[4])
#         listAlumnos.append(alumno)
        
#     for alumno in listAlumnos:
#         print(alumno)
# obtenerListaAlumnos()

try:
    MenuPrincipal = {"Alumnos": "1", "Profesores": "2","Salones": "3","Cursos":"4","Salir": "0"}
    showHome = True
    seleccion = ""
    menuPrincipal = Menu("Principal", MenuPrincipal)

    while showHome:
        seleccion = menuPrincipal.show()
        if(seleccion == "0"):
            break

        if(seleccion == "1"):
            opcAlumnos = {"Listar Alumnos": "1", "Registrar Alumno": "2","Editar Alumno": "3","Eliminar Alumno":"4","Salir": "0"}
            seleccionMenuAlumno = ""
            menuAlumnos = Menu("Alumnos", opcAlumnos)
            seleccionMenuAlumno = menuAlumnos.show()

            AlumnoBD = AlumnoBD()

            if (seleccionMenuAlumno == "1"):
                AlumnoBD.mostrarLista()
            if (seleccionMenuAlumno == "2"):
                AlumnoBD.registrar()               
            if (seleccionMenuAlumno == "3"):
                AlumnoBD.actualizar()               
            if (seleccionMenuAlumno == "4"):
                AlumnoBD.eliminar()               

        if(seleccion == "2"):
            opMenuProfesores = {"Mostrar Profesores": "1", "Registrar Profesor": "2","Editar Profesor": "3","Eliminar Profesor":"4","Salir": "0"}
            ansProfesores = ""
            menuProfesores = Menu("Profesores", opMenuProfesores)
            ansProfesores = menuProfesores.show()
            if (ansProfesores == "1"):
                Profesor.listarProfesor()
            if (ansProfesores == "2"):
                Profesor.crearProfesor()               
            if (ansProfesores == "3"):
                Profesor.editarProfesor()               
            if (ansProfesores == "4"):
                Profesor.eliminarProfesor()

        if(seleccion == "3"):
            opMenuSalon = {"Mostrar Salones": "1", "Registrar Salon": "2","Editar Salon": "3","Eliminar Salon":"4","Salir": "0"}
            ansSalones = ""
            menuPSalones = Menu("Salones", opMenuSalon)
            ansSalones = menuPSalones.show()
            if (ansSalones == "1"):
                Salon.listarSalon()
            if (ansSalones == "2"):
                Salon.crearSalon()               
            if (ansSalones == "3"):
                Salon.editarSalon()               
            if (ansSalones == "4"):
                Salon.eliminarSalon()

        if(seleccion == "4"):
            opMenuCurso = {"Mostrar Cursos": "1", "Registros Curso": "2","Editar Curso": "3","Eliminar Curso":"4","Salir": "0"}
            ansSalones = ""
            menuCursos = Menu("Cursos", opMenuCurso)
            ansCursos = menuCursos.show()
            if (ansCursos == "1"):
                Curso.listarCurso()
            if (ansCursos == "2"):
                Curso.crearCurso()               
            if (ansCursos == "3"):
                Curso.editarCurso()               
            if (ansCursos == "4"):
                Curso.eliminarCurso()

except Exception as error:
    print(str(error))