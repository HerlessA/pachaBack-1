from utils import Menu
from salon import Salon
from curso import Curso
from alumno import Alumno
from profesor import Profesor


try:
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
                
                Alumno.listarAlumno()
            if (ansAlumnos == "2"):
                Alumno.crearAlumno()               
            if (ansAlumnos == "3"):
                Alumno.editarAlumno()               
            if (ansAlumnos == "4"):
                Alumno.eliminarAlumno()

        if(ansMenuPrincipal == "2"):
            opMenuProfesores = {"Listar Profesores": "1", "Crear Profesor": "2","Editar Profesor": "3","Eliminar Profesor":"4","Salir": "0"}
            ansProfesores = ""
            menuProfesores = Menu("Profesores", opMenuProfesores)
            ansProfesores = menuProfesores.show()
            if (ansProfesores == "1"):
                Profesor.cargarProfesor()
                Profesor.listarProfesor()
            if (ansProfesores == "2"):
                Profesor.crearProfesor()               
            if (ansProfesores == "3"):
                Profesor.editarProfesor()               
            if (ansProfesores == "4"):
                Profesor.eliminarProfesor()

        if(ansMenuPrincipal == "3"):
            opMenuSalon = {"Listar Salones": "1", "Crear Salon": "2","Editar Salon": "3","Eliminar Salon":"4","Salir": "0"}
            ansSalones = ""
            menuPSalones = Menu("Salones", opMenuSalon)
            ansSalones = menuPSalones.show()
            if (ansSalones == "1"):
                Salon.cargarSalon()
                Salon.listarSalon()
            if (ansSalones == "2"):
                Salon.crearSalon()               
            if (ansSalones == "3"):
                Salon.editarSalon()               
            if (ansSalones == "4"):
                Salon.eliminarSalon()

        if(ansMenuPrincipal == "4"):
            opMenuCurso = {"Listar Cursos": "1", "Crear Curso": "2","Editar Curso": "3","Eliminar Curso":"4","Salir": "0"}
            ansSalones = ""
            menuCursos = Menu("Cursos", opMenuCurso)
            ansCursos = menuCursos.show()
            if (ansCursos == "1"):
                Curso.cargarCurso()
                Curso.listarCurso()
            if (ansCursos == "2"):
                Curso.crearCurso()               
            if (ansCursos == "3"):
                Curso.editarCurso()               
            if (ansCursos == "4"):
                Curso.eliminarCurso()

except Exception as error:
    print(str(error))