from utils import Menu
from alumno import *
from profesor import *
import os

def limpiarPantalla():
        def clear():
            # return os.system('cls')
            return os.system('clear')
        clear()

def menuAlumno():
    ansMenuAlumno = ""
    opMenuAlumno = {"Crear Alumno" : "1", "Mostrar Lista de Alumnos" : "2", "Buscar Alumno" : "3", "Editar Alumno" : "4", "Eliminar Alumno" : "5", "Asignar Salon" : "6", "Asignar Nota" : "7", "Volver Menu Principal" : "0"}
    menuAlumno = Menu("Alumno", opMenuAlumno)
    while ansMenuAlumno != 0:
        ansMenuAlumno = menuAlumno.show()
        if(ansMenuAlumno == "1"):
            limpiarPantalla()
            crearAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "2"):
            limpiarPantalla()
            listarAlumnos()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "3"):
            limpiarPantalla()
            buscarAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "4"):
            limpiarPantalla()
            actualizarAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "5"):
            limpiarPantalla()
            eliminarAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "6"):
            ansMenuSalonAlumno = ""
            opMenuSalonAlumno = {"Asignar Salon a un Alumno" : "1", "Eliminar Salon de un Alumno" : "2", "Volver Menu Anterior" : "0"}
            menuSalonAlumno = Menu("Salon Alumno", opMenuSalonAlumno)
            while ansMenuSalonAlumno != 0:
                ansMenuSalonAlumno = menuSalonAlumno.show()
                if(ansMenuSalonAlumno == "1"):
                    limpiarPantalla()
                    asignarSalonesAl()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonAlumno == "2"):
                    limpiarPantalla()
                    eliminarSalonesAl()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonAlumno == "0"):
                    break                   
        if(ansMenuAlumno == "7"):
            ansMenuNotaAlumno = ""
            opMenuNotaAlumno = {"Asignar Nota a un Alumno" : "1", "Eliminar Notas de un Alumno" : "2", "Volver Menu Anterior" : "0"}
            menuNotaAlumno = Menu("Nota Alumno", opMenuNotaAlumno)
            while ansMenuNotaAlumno != 0:
                ansMenuNotaAlumno = menuNotaAlumno.show()
                if(ansMenuNotaAlumno == "1"):
                    limpiarPantalla()
                    asignarNotas()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaAlumno == "2"):
                    limpiarPantalla()
                    eliminarNotas()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaAlumno == "0"):
                    break
        if(ansMenuAlumno == "0"):
            break                  

def menuProfesor():
    ansMenuProfesor = ""
    opMenuProfesor = {"Crear Profesor" : "1", "Mostrar Lista de Profesores" : "2", "Buscar Profesor" : "3", "Editar Profesor" : "4", "Eliminar Profesor" : "5", "Asignar Salon" : "6", "Asignar Nota" : "7", "Volver Menu Principal" : "0"}
    menuProfesor = Menu("Profesor", opMenuProfesor)
    while ansMenuProfesor != 0:
        ansMenuProfesor = menuProfesor.show()
        if(ansMenuProfesor == "1"):
            limpiarPantalla()
            crearProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "2"):
            limpiarPantalla()
            listarProfesores()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "3"):
            limpiarPantalla()
            buscarProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "4"):
            limpiarPantalla()
            actualizarProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "5"):
            limpiarPantalla()
            eliminarProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "6"):
            ansMenuSalonProfesor = ""
            opMenuSalonProfesor = {"Asignar Salon a un Profesor" : "1", "Eliminar Salon de un Profesor" : "2", "Volver Menu Anterior" : "0"}
            menuSalonProfesor = Menu("Salon Profesor", opMenuSalonProfesor)
            while ansMenuSalonProfesor != 0:
                ansMenuSalonProfesor = menuSalonProfesor.show()
                if(ansMenuSalonProfesor == "1"):
                    limpiarPantalla()
                    asignarSalonesProf()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonProfesor == "2"):
                    limpiarPantalla()
                    eliminarSalonesProf()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonProfesor == "0"):
                    break                   
        if(ansMenuProfesor == "7"):
            ansMenuCursoProfesor = ""
            opMenuCursoProfesor = {"Asignar Curso a un Profesor" : "1", "Eliminar Curso de un Profesor" : "2", "Volver Menu Anterior" : "0"}
            menuCursoProfesor = Menu("Curso Profesor", opMenuCursoProfesor)
            while ansMenuCursoProfesor != 0:
                ansMenuCursoProfesor = menuCursoProfesor.show()
                if(ansMenuCursoProfesor == "1"):
                    limpiarPantalla()
                    asignarCursos()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuCursoProfesor == "2"):
                    limpiarPantalla()
                    eliminarCursos()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuCursoProfesor == "0"):
                    break
        if(ansMenuProfesor == "0"):
            break                  

try:
    opMenuPrincipal = {"Alumnos" : "1", "Profesores" : "2", "Salir" : "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            menuAlumno()
            continue
        if(ansMenuPrincipal == "2"):
            menuProfesor()
            continue
except Exception as error:
    print(str(error))


