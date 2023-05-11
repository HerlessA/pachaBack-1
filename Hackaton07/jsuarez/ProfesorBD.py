from conexion import conexion
from tabulate import tabulate
from Profesor import Profesor
from conexionMBD import ConexionMBD


class ProfesorBD():

    lista = []
    # conexion = conexion()
    conexion = ConexionMBD("mongodb://localhost:27017","bds7")

    def mostrarLista(self):
        resultado = self.conexion.obtener_registros("profesor")
        header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))

    def registrar(self):
        try:
            IdentificadorProfesor = input("Identificador: ")
            Nombre = input("Nombre: ")
            Edad = int(input("Edad: "))
            Correo = input("Correo electrónico: ")
            profesor = Profesor(IdentificadorProfesor,Nombre,Edad,Correo)
            if(self.conexion.insertar_registro("profesor",profesor.__dict__)):
                print("Se ha creado el Profesor")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador del profesor : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("profesor",condicion)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)

            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")

            nuevos_valores = {"$set": {"nombre": nombre,"edad":edad, "correo": correo}}

            if(self.conexion.actualizar_registro("profesor",condicion,nuevos_valores)):
                ProfesorBD.mostrarLista(self)
                print("Se ha actualzado el profesor")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos",ex)


    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador del profesor : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("profesor",condicion)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)

            if(self.conexion.borrar_registro("profesor",condicion)):
                ProfesorBD.mostrarLista(self)
                print("Se ha eliminado el profesor")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos",ex)