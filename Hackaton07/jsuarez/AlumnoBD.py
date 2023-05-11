from conexion import conexion
from tabulate import tabulate
from Alumno import Alumno
from conexionMBD import ConexionMBD

# conn = ConexionMBD("mongodb://localhost:27017","bds7")


class AlumnoBD():

    lista = []
    # conexion = conexion()
    conexion = ConexionMBD("mongodb://localhost:27017","bds7")

    def mostrarLista(self):
        resultado = self.conexion.obtener_registros("alumnos")
        header = ['ID','IdentificadorAlumno','Nombre','edad','correo']
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))

    def registrar(self):
        try:
            IdentificadorAlumno = input("Identificador: ")
            Nombre = input("Nombre: ")
            Edad = int(input("Edad: "))
            Correo = input("Correo electrónico: ")

            alumno = Alumno(IdentificadorAlumno,Nombre,Edad,Correo)

            self.conexion.insertar_registro("alumnos",alumno.__dict__)
            
            print("Se ha creado el Alumno")
            input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador del alumno : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("alumnos",condicion)
            header = ['ID','IdentificadorAlumno','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)

            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")

            nuevos_valores = {"$set": {"nombre": nombre,"edad":edad, "correo": correo}}

            if(self.conexion.actualizar_registro("alumnos",condicion,nuevos_valores)):
                AlumnoBD.mostrarLista(self)
                print("Se ha actualzado al alumno")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos",ex)


    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador del alumno : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("alumnos",condicion)
            header = ['ID','IdentificadorAlumno','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))

            if(self.conexion.borrar_registro("alumnos",condicion)):
                AlumnoBD.mostrarLista(self)
                print("Se ha borrado al alumno")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")  
        except Exception as ex:
            print("Error al ingresar los datos",ex)