from conexion import conexion
from tabulate import tabulate
from Salon import Salon
from CursoBD import CursoBD


class SalonBD():

    lista = []
    conexion = conexion()
    CursoBD = CursoBD()

    def mostrarLista(self):
        self.lista = []
        query = "select * from salon;"
        resultado = self.conexion.consultarBDD(query=query)

        for sal in resultado:
            salon = Salon(sal[0], sal[1], sal[2], sal[3])
            self.lista.append(salon)

        for salon in self.lista:
            print(salon)

    def registrar(self):
        try:
            IdentificadorSalon = input("Identificador: ")
            Nombre = input("Nombre: ")
            AnioEscolar = int(input("Anio: "))

            salon = Salon(None, Nombre, AnioEscolar, IdentificadorSalon)

            query = f'''insert into salon(nombre,identificadorsalon,anioescolar)
                    values('{salon.Nombre}','{salon.IdentificadorSalon}',{salon.AnioEscolar});'''

            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha creado el salon")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador : ")
            query = f"select * from salon where identificadorsalon = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdSalon', 'Identificadorsalon',
                      'Nombre', 'Anio Escolar']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            nombre = input("Nombre: ")
            anioescolar = int(input("Año escolar: "))

            query2 = f'''update salon
                    set nombre = '{nombre}',
                    anioescolar = {anioescolar}
                    where identificadorsalon = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                SalonBD.mostrarLista(self)
                print("Se ha actualzado el salon")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador : ")
            query = f"select * from salon where identificadorsalon = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdSalon', 'Nombre',
                      'Anio Escolar', 'IdentificadorSalon']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            query2 = f''' delete from salon
                where identificadorsalon = '{identificador}';'''
            if(self.conexion.ejecutarBDD(query=query2)):
                SalonBD.mostrarLista(self)
                print("Se ha eliminado al Salon")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def asignarCurso(self):
        try:

            # listar cursos
            CursoBD.mostrarLista(self)
            # fin listar cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso', 'Nombre', 'identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial profesor
            pkCurso = resultado[0][0]
            # fin obtener serial profesor

            # lista salon
            SalonBD.mostrarLista(self)
            # fin lista salon

            # seleccionar salon
            identificador = input("Ingrese el identificador : ")
            query = f"select * from salon where identificadorsalon = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdSalon', 'nombre',
                      'Anio escolar', 'identificadorsalon']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar salon

            # obtener serial salon
            pkSalon = resultado[0][0]
            # fin obtener serial salon

            # asignar curso a salon
            query = f'''insert into salon_curso(idsalon,idcurso)
                    values('{pkSalon}', '{pkCurso}');'''

            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha asignado el curso")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def desasignarCurso(self):
        try:

            # listar cursos
            CursoBD.mostrarLista(self)
            # fin listar cursos

            # seleccionar curso
            identificador = input("Ingrese el identificador : ")
            query = f"select * from cursos where identificadorcurso = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdCurso', 'Nombre', 'identificadorcurso']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar curso

            # obtener serial profesor
            pkCurso = resultado[0][0]
            # fin obtener serial profesor

            # lista salon
            SalonBD.mostrarLista(self)
            # fin lista salon

            # seleccionar salon
            identificador = input("Ingrese el identificador : ")
            query = f"select * from salon where identificadorsalon = '{identificador}';"
            resultado = self.conexion.consultarBDD(query=query)
            header = ['IdSalon', 'nombre',
                      'Anio escolar', 'identificadorsalon']
            print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar salon

            # obtener serial salon
            pkSalon = resultado[0][0]
            # fin obtener serial salon

            # desasignar curso de salon
            query = f'''delete from salon_curso where idsalon =
                    '{pkSalon}' and  idcurso= '{pkCurso}';'''

            if(self.conexion.ejecutarBDD(query=query)):
                print("Se ha desasignado el curso")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def mostrarCursosPorSalon(self):
        self.lista = []
        # lista salon
        SalonBD.mostrarLista(self)
        # fin lista salon

        # seleccionar salon
        identificador = input("Ingrese el identificador : ")
        query = f"select * from salon where identificadorsalon = '{identificador}';"
        resultado = self.conexion.consultarBDD(query=query)
        header = ['IdSalon', 'Identificadorsalon',
                  'Nombre', 'Anio Escolar']
        print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar salon

        # obtener serial salon
        pkSalon = resultado[0][0]
        # fin obtener serial salon

        query = f"SELECT C.* FROM salon_curso SC INNER JOIN CURSOS C ON SC.idCurso = C.idCurso where SC.idSalon = '{pkSalon}';"
        resultado = self.conexion.consultarBDD(query=query)

        print("Cursos asignados al salon")

        header = ['IdCurso','nombre','identificadorcurso']
        print(tabulate(resultado, headers=header, tablefmt='fancy_grid'))
