from conexion import conexion
from tabulate import tabulate
from Profesor import Profesor


class ProfesorBD():

    lista = []
    conexion = conexion()

    def mostrarLista(self):
        self.lista = []
        query = "select * from profesor;"
        resultado = self.conexion.consultarBDD(query=query)

        for profe in resultado:
            profesor = Profesor(profe[0], profe[1], profe[2], profe[3], profe[4])
            self.lista.append(profesor)

        for profesor in self.lista:
            print(profesor)

    def registrar(self):
        try:
            IdentificadorProfesor = input("Identificador: ")
            Nombre = input("Nombre: ")
            Edad = int(input("Edad: "))
            Correo = input("Correo electrónico: ")

            profesor = Profesor(None,IdentificadorProfesor,Nombre,Edad,Correo)

            query = f'''insert into profesor(nombre,IdentificadorProfesor,edad,correo)
                    values('{profesor.Nombre}','{profesor.IdentificadorProfesor}',{profesor.Edad},'{profesor.Correo}');'''
            
            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha creado el Profesor")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador : ")
            query = f"select * from profesor where identificadorProfesor = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")

            query2 = f'''update profesor
                    set nombre = '{nombre}',
                    edad = {edad},
                    correo = '{correo}'
                    where identificadorProfesor = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                ProfesorBD.mostrarLista(self)
                print("Se ha actualzado al profesor")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)


    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador : ")
            query = f"select * from profesor where identificadorProfesor = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdProfesor','IdentificadorProfesor','Nombre','edad','correo']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            query2 = f''' delete from profesor
                where identificadorProfesor = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                ProfesorBD.mostrarLista(self)
                print("Se ha eliminado al Profesor")
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)