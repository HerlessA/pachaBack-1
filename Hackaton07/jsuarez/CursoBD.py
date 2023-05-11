from conexion import conexion
from tabulate import tabulate
from Curso import Curso
from Alumno import Alumno
from AlumnoBD import AlumnoBD
from ProfesorBD import ProfesorBD
from conexionMBD import ConexionMBD


class CursoBD():

    lista = []
    # conexion = conexion()
    conexion = ConexionMBD("mongodb://localhost:27017", "bds7")

    AlumnoBD = AlumnoBD()
    ProfesorBD = ProfesorBD()

    def mostrarLista(self):
        resultado = self.conexion.obtener_registros("cursos")
        header = ['ID', 'identificador', 'nombre']
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))

    def registrar(self):
        try:
            identificador = input("Identificador: ")
            Nombre = input("Nombre: ")

            alumno = Curso(identificador, Nombre)

            self.conexion.insertar_registro("cursos", alumno.__dict__)

            print("Se ha creado el Curso")
            input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            nombre = input("Nombre: ")
            nuevos_valores = {"$set": {"nombre": nombre}}

            if(self.conexion.actualizar_registro("cursos", condicion, nuevos_valores)):
                CursoBD.mostrarLista(self)
                print("Se ha actualzado al curso")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)

            if(self.conexion.borrar_registro("cursos", condicion)):
                CursoBD.mostrarLista(self)
                print("Se ha eliminado al curso")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def asignarAlumno(self):
        try:

            # listar alumnos
            AlumnoBD.mostrarLista(self)
            # fin listar alumnos

            # seleccionar alumno
            identificador = input("Ingrese el identificador del alumno : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("alumnos",condicion)
            header = ['ID','IdentificadorAlumno','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            # fin seleccionar alumno

            # obtener serial alumno
            pkAlumno = registros[0][0]
            # fin obtener serial alumno


            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso = registros[0][0]
            # fin obtener serial curso

            curso_alumno = {
                "idCurso": pkCurso,
                "idAlumno": pkAlumno
            }

            if self.conexion.insertar_registro("curso_alumno",curso_alumno):
                print("Se ha asignado el alumno")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def deasignarAlumno(self):
        try:

            # listar alumnos
            AlumnoBD.mostrarLista(self)
            # fin listar alumnos

            # seleccionar alumno
            identificador = input("Ingrese el identificador del alumno : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("alumnos",condicion)
            header = ['ID','IdentificadorAlumno','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            # fin seleccionar alumno

            # obtener serial alumno
            pkAlumno = registros[0][0]
            # fin obtener serial alumno


            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso = registros[0][0]
            # fin obtener serial curso

            curso_alumno = {
                "idCurso": pkCurso,
                "idAlumno": pkAlumno
            }

            if self.conexion.borrar_registro("curso_alumno",curso_alumno):
                print("Se ha desasignado el alumno")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def mostrarAlumnosPorCurso(self):
        self.lista = []
        # lista cursos
        CursoBD.mostrarLista(self)
        # fin lista cursos

        # seleccionar curso
        identificador = input("Ingrese el identificador del curso : ")
        condicion = {"identificador": identificador}
        resultado = self.conexion.obtener_registros("cursos", condicion)
        header = ['IdCurso', 'identificadorcurso', 'nombre']
        # Lista de listas con los valores de los registros
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar curso

        # obtener serial curso
        pkCurso = registros[0][0]
        # fin obtener serial curso

        # seleccionar curso
        condicion = {"idCurso": pkCurso}
        resultado = self.conexion.obtener_registros("curso_alumno", condicion)
        header = ['id', 'idCurso', 'idAlumno']
        # Lista de listas con los valores de los registros
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar curso

        for registro in registros:
            pkAlumno = registro[2]
            condicion = {"_id": pkAlumno}
            resultado = self.conexion.obtener_registros("alumnos", condicion)
            header = ['ID','IdentificadorAlumno','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado]

            print("Alumno")
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))

    def asignarProfesor(self):
        try:

            # listar alumnos
            ProfesorBD.mostrarLista(self)
            # fin listar alumnos

            # seleccionar alumno
            identificador = input("Ingrese el identificador del profesor : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("profesor",condicion)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            # fin seleccionar alumno

            # obtener serial alumno
            pkProfesor = registros[0][0]
            # fin obtener serial alumno

            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso = registros[0][0]
            # fin obtener serial curso

            curso_profesor = {
                "idCurso": pkCurso,
                "idProfesor": pkProfesor
            }

            if self.conexion.insertar_registro("curso_profesor",curso_profesor):
                print("Se ha asignado el profesor")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def deasignarProfesor(self):
        try:

            # listar alumnos
            ProfesorBD.mostrarLista(self)
            # fin listar alumnos

            # seleccionar alumno
            identificador = input("Ingrese el identificador del profesor : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("profesor",condicion)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            # fin seleccionar alumno

            # obtener serial alumno
            pkProfesor = registros[0][0]
            # fin obtener serial alumno

            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso = registros[0][0]
            # fin obtener serial curso

            curso_profesor = {
                "idCurso": pkCurso,
                "idProfesor": pkProfesor
            }

            if self.conexion.borrar_registro("curso_profesor",curso_profesor):
                print("Se ha desasignado el PROFESOR")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)


    def mostrarProfesorPorCurso(self):
        self.lista = []
        # lista cursos
        CursoBD.mostrarLista(self)
        # fin lista cursos

        # seleccionar curso
        identificador = input("Ingrese el identificador del curso : ")
        condicion = {"identificador": identificador}
        resultado = self.conexion.obtener_registros("cursos", condicion)
        header = ['IdCurso', 'identificadorcurso', 'nombre']
        # Lista de listas con los valores de los registros
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar curso

        # obtener serial curso
        pkCurso = registros[0][0]
        # fin obtener serial curso

        # seleccionar curso
        condicion = {"idCurso": pkCurso}
        resultado = self.conexion.obtener_registros("curso_profesor", condicion)
        header = ['id', 'idCurso', 'idProfesor']
        # Lista de listas con los valores de los registros
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar curso

        for registro in registros:
            pkProfesor = registro[2]
            condicion = {"_id": pkProfesor}
            resultado = self.conexion.obtener_registros("profesor", condicion)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado]

            print("Profesor")
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))