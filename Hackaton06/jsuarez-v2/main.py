from utils import Menu
from Alumno import Alumno
from AlumnoBD import AlumnoBD
from ProfesorBD import ProfesorBD
from CursoBD import CursoBD
from SalonBD import SalonBD
from tabulate import TableFormat, tabulate


try:
    MenuPrincipal = {"Alumnos": "1", "Profesores": "2",
                     "Salones": "3", "Cursos": "4", "Salir": "0"}
    showHome = True
    seleccion = ""
    menuPrincipal = Menu("Principal", MenuPrincipal)

    AlumnoBD = AlumnoBD()
    ProfesorBD = ProfesorBD()
    CursoBD = CursoBD()
    SalonBD = SalonBD();

    while showHome:
        seleccion = menuPrincipal.show()
        if(seleccion == "0"):
            break

        if(seleccion == "1"):
            opcionesAlumno = {"Listar Alumnos": "1", "Registrar Alumno": "2",
                              "Editar Alumno": "3", "Eliminar Alumno": "4", "Salir": "0"}
            seleccionMenuAlumno = ""
            menuAlumnos = Menu("Alumnos", opcionesAlumno)
            seleccionMenuAlumno = menuAlumnos.show()

            if (seleccionMenuAlumno == "1"):
                AlumnoBD.mostrarLista()
            if (seleccionMenuAlumno == "2"):
                AlumnoBD.registrar()
            if (seleccionMenuAlumno == "3"):
                AlumnoBD.actualizar()
            if (seleccionMenuAlumno == "4"):
                AlumnoBD.eliminar()

        if(seleccion == "2"):
            opcionesProfesor = {"Mostrar Profesores": "1", "Registrar Profesor": "2",
                                "Editar Profesor": "3", "Eliminar Profesor": "4", "Salir": "0"}
            ansProfesores = ""
            menuProfesores = Menu("Profesores", opcionesProfesor)
            ansProfesores = menuProfesores.show()
            if (ansProfesores == "1"):
                ProfesorBD.mostrarLista()
            if (ansProfesores == "2"):
                ProfesorBD.registrar()
            if (ansProfesores == "3"):
                ProfesorBD.actualizar()
            if (ansProfesores == "4"):
                ProfesorBD.eliminar()

        if(seleccion == "3"):
            opcionesSalon = {"Mostrar Salones": "1", "Registrar Salon": "2",
                             "Editar Salon": "3", "Eliminar Salon": "4", "Asignar curso": "5", "Desasignar curso": "6", "Mostrar cursos por Salon": "7", "Salir": "0"}
            ansSalones = ""
            menuPSalones = Menu("Salones", opcionesSalon)
            ansSalones = menuPSalones.show()
            if (ansSalones == "1"):
                SalonBD.mostrarLista()
            if (ansSalones == "2"):
                SalonBD.registrar()
            if (ansSalones == "3"):
                SalonBD.actualizar()
            if (ansSalones == "4"):
                SalonBD.eliminar()
            if (ansSalones == "5"):
                SalonBD.asignarCurso()
            if (ansSalones == "6"):
                SalonBD.desasignarCurso()
            if (ansSalones == "7"):
                SalonBD.mostrarCursosPorSalon()

        if(seleccion == "4"):
            opcionesCurso = {"Mostrar Cursos": "1", "Registros Curso": "2", "Editar Curso": "3", "Eliminar Curso": "4", "Asignar alumno": "5", "Desasignar alumno": "6","Mostar alumnos por curso": "7", "Asignar profesor": "8", "Desasignar profesor": "9", "Mostar profesor por curso": "10", "Salir": "0"}
            ansSalones = ""
            menuCursos = Menu("Cursos", opcionesCurso)
            ansCursos = menuCursos.show()
            if (ansCursos == "1"):
                CursoBD.mostrarLista()
            if (ansCursos == "2"):
                CursoBD.registrar()
            if (ansCursos == "3"):
                CursoBD.actualizar()
            if (ansCursos == "4"):
                CursoBD.eliminar()
            if (ansCursos == "5"):
                CursoBD.asignarAlumno()
            if (ansCursos == "6"):
                CursoBD.deasignarAlumno()
            if (ansCursos == "7"):
                CursoBD.mostrarAlumnosPorCurso()
            if (ansCursos == "8"):
                CursoBD.asignarProfesor()
            if (ansCursos == "9"):
                CursoBD.deasignarProfesor()
            if (ansCursos == "10"):
                CursoBD.mostrarProfesorPorCurso()

except Exception as error:
    print(str(error))
