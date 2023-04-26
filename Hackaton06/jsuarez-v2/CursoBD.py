from conexion import conexion
from tabulate import tabulate
from Curso import Curso
from Alumno import Alumno
from AlumnoBD import AlumnoBD
from ProfesorBD import ProfesorBD


class CursoBD():

    lista = []
    lista = []
    conexion = conexion()
    AlumnoBD = AlumnoBD()
    ProfesorBD = ProfesorBD()

    def mostrarLista(self):
        self.lista = []
        query = "select * from cursos;"
        resultado = self.conexion.consultarBDD(query=query)

        for curs in resultado:
            curso = Curso(curs[0], curs[1], curs[2])
            self.lista.append(curso)

        for curso in self.lista:
            print(curso)

    def registrar(self):
        try:
            Identificador = input("Identificador: ")
            Nombre = input("Nombre: ")
            
            curso = Curso(None,Nombre,Identificador)

            query = f'''insert into cursos(nombre,identificadorcurso)
                    values('{curso.Nombre}', '{curso.IdentificadorCurso}');'''
            
            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha creado el Curso")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso','nombre','identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))

            Nombre = input("Nombre: ")

            query2 = f'''update cursos 
                    set nombre = '{Nombre}'
                    where identificadorcurso = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                CursoBD.mostrarLista(self)
                print("Se ha actualzado al Curso")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)


    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso','nombre','identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))

            query2 = f''' delete from cursos
                where identificadorcurso = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                CursoBD.mostrarLista(self)
                print("Se ha eliminado al Curso")
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)

    def asignarAlumno(self):
        try:
            
            # listar alumnos
            AlumnoBD.mostrarLista(self)
            # fin listar alumnos

            # seleccionar alumno
            identificador = input("Ingrese el identificador : ")
            query = f"select * from alumnos where identificadoralumno = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdAlumno','Identificadoralumno','Nombre','Edad','Correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar alumno

            # obtener serial alumno
            pkAlumno =  resultado[0][0]
            # fin obtener serial alumno

            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso','nombre','identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso =  resultado[0][0]
            # fin obtener serial curso

            # asignar alumno a curso
            query = f'''insert into curso_alumno(idcurso,idalumno)
                    values('{pkCurso}', '{pkAlumno}');'''
            
            if(self.conexion.ejecutarBDD(query=query)):
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
            identificador = input("Ingrese el identificador : ")
            query = f"select * from alumnos where identificadoralumno = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdAlumno','Identificadoralumno','Nombre','Edad','Correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar alumno

            # obtener serial alumno
            pkAlumno =  resultado[0][0]
            # fin obtener serial alumno

            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso','nombre','identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso =  resultado[0][0]
            # fin obtener serial curso

            # desasignar alumno a curso
            query = f'''delete from curso_alumno where idCurso = 
                    '{pkCurso}' and  idAlumno = '{pkAlumno}';'''
            
            if(self.conexion.ejecutarBDD(query=query)):
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
        identificador = input("Ingrese el identificador : ")
        query = f"select * from cursos where identificadorcurso = '{identificador}';"
        resultado = self.conexion.consultarBDD(query=query)
        header = ['IdCurso','nombre','identificadorcurso']
        print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar curso

        # obtener serial curso
        pkCurso =  resultado[0][0]
        # fin obtener serial curso

        query = f"SELECT A.* FROM CURSO_ALUMNO CA INNER JOIN ALUMNOS A ON CA.idAlumno = A.idAlumno WHERE CA.idCurso = '{pkCurso}';"
        resultado = self.conexion.consultarBDD(query=query)

        print("Lista de alumnos asignados al curso")

        header = ['idAlumno','IdentificadorAlumno','Nombre','edad','correo']
        print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))

    def asignarProfesor(self):
        try:
            
            # listar profesores
            ProfesorBD.mostrarLista(self)
            # fin listar profesores

            # seleccionar profesor
            identificador = input("Ingrese el identificador : ")
            query = f"select * from profesor where identificadorprofesor = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','Edad','Correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar profesor

            # obtener serial profesor
            pkProfesor =  resultado[0][0]
            # fin obtener serial profesor

            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso','nombre','identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso =  resultado[0][0]
            # fin obtener serial curso

            # asignar profesor a curso
            query = f'''insert into curso_profesor(idcurso,idprofesor)
                    values('{pkCurso}', '{pkProfesor}');'''
            
            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha asignado el profesor")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def deasignarProfesor(self):
        try:
            
            # listar profesores
            ProfesorBD.mostrarLista(self)
            # fin listar profesores

            # seleccionar profesor
            identificador = input("Ingrese el identificador : ")
            query = f"select * from profesor where identificadorprofesor = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','Edad','Correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar profesor

            # obtener serial profesor
            pkProfesor =  resultado[0][0]
            # fin obtener serial profesor

            # lista cursos
            CursoBD.mostrarLista(self)
            # fin lista cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso','nombre','identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial curso
            pkCurso =  resultado[0][0]
            # fin obtener serial curso

            # desasignar profesor a curso
            query = f'''delete from curso_profesor where idCurso = 
                    '{pkCurso}' and  idprofesor= '{pkProfesor}';'''
            
            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha desasignado el profesor")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def mostrarProfesorPorCurso(self):
        self.lista = []
        # lista cursos
        CursoBD.mostrarLista(self)
        # fin lista cursos

        # seleccionar curso
        identificador = input("Ingrese el identificador : ")
        query = f"select * from cursos where identificadorcurso = '{identificador}';"
        resultado = self.conexion.consultarBDD(query=query)
        header = ['IdCurso','nombre','identificadorcurso']
        print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar curso

        # obtener serial curso
        pkCurso =  resultado[0][0]
        # fin obtener serial curso

        query = f"SELECT P.* FROM CURSO_PROFESOR CP INNER JOIN PROFESOR P ON CP.idProfesor = P.idProfesor WHERE CP.idCurso =  '{pkCurso}';"
        resultado = self.conexion.consultarBDD(query=query)

        print("Profesores asignados al curso")

        header = ['idAlumno','IdentificadorAlumno','Nombre','edad','correo']
        print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))