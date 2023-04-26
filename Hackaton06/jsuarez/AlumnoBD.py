from conexion import conexion
from tabulate import tabulate
from Alumno import Alumno


class AlumnoBD():

    lista = []
    conexion = conexion()

    # def __init__(self, alumno):
    #     self.alumno = alumno

    def mostrarLista(self):
        query = "select * from alumnos;"
        resultado = self.conexion.consultarBDD(query=query)

        for alumn in resultado:
            alumno = Alumno(alumn[0], alumn[1], alumn[2], alumn[3], alumn[4])
            self.lista.append(alumno)

        for alumno in AlumnoBD.lista:
            print(alumno)

    def registrar(self):
        try:
            IdentificadorAlumno = input("Identificador: ")
            Nombre = input("Nombre de Alumno: ")
            Edad = int(input("Edad: "))
            Correo = input("Correo electrónico: ")

            alumno = Alumno(None,IdentificadorAlumno,Nombre,Edad,Correo)

            query = f'''insert into alumnos(nombre,IdentificadorAlumno,edad,correo)
                    values('{alumno.Nombre}','{alumno.IdentificadorAlumno}',{alumno.Edad},'{alumno.Correo}');'''
            
            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha creado el Alumno")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador del alumno : ")
            query = f"select * from alumnos where identificadorAlumno = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['idAlumno','IdentificadorAlumno','Nombre','edad','correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            nombre = input("Nombre de Alumno: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")

            query2 = f'''update alumnos 
                    set nombre = '{nombre}',
                    edad = {edad},
                    correo = '{correo}'
                    where identificadorAlumno = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                AlumnoBD.mostrarLista(self)
                print("Se ha actualzado al alumno")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)


    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador del alumno : ")
            query = f"select * from alumnos where identificadorAlumno = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['idAlumno','IdentificadorAlumno','Nombre','edad','correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            query2 = f''' delete from alumnos
                where identificadorAlumno = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                AlumnoBD.listarAlumno()
                print("Se ha eliminado al Alumno")
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)