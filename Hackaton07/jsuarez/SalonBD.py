from conexion import conexion
from tabulate import tabulate
from Salon import Salon
from CursoBD import CursoBD
from conexionMBD import ConexionMBD


class SalonBD():

    lista = []
    # conexion = conexion()
    conexion = ConexionMBD("mongodb://localhost:27017", "bds7")

    CursoBD = CursoBD()

    def mostrarLista(self):
        resultado = self.conexion.obtener_registros("salon")
        header = ['IdSalon', 'Identificadorsalon',
                  'Nombre', 'Anio Escolar']
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))

    def registrar(self):
        try:
            identificador = input("Identificador: ")
            Nombre = input("Nombre: ")
            AnioEscolar = input("Año Escolar: ")

            salon = Salon(identificador, Nombre,AnioEscolar)

            self.conexion.insertar_registro("salon", salon.__dict__)

            print("Se ha creado el Salon")
            input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def actualizar(self):
        try:
            identificador = input("Ingrese el identificador del salon : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("salon", condicion)
            header = ['IdSalon', 'Nombre',
                      'Anio Escolar', 'IdentificadorSalon']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            nombre = input("Nombre: ")
            anioescolar = input("Año escolar: ")
            nuevos_valores = {"$set": {"nombre": nombre,"anioescolar":anioescolar}}

            if(self.conexion.actualizar_registro("salon", condicion, nuevos_valores)):
                SalonBD.mostrarLista(self)
                print("Se ha actualzado al salon")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def eliminar(self):
        try:
            identificador = input("Ingrese el identificador del salon : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("salon", condicion)
            header = ['IdSalon', 'Nombre',
                      'Anio Escolar', 'IdentificadorSalon']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)

            if(self.conexion.borrar_registro("salon", condicion)):
                SalonBD.mostrarLista(self)
                print("Se ha eliminado al salon")
                input("¿Desea Continuar S/N? -> ")
            else:
                print("Ocurrio un problema")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def asignarCurso(self):
        try:

            # listar cursos
            CursoBD.mostrarLista(self)
            # fin listar cursos

            # seleccionar alumno
            identificador = input("Ingrese el identificador del Curso : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("cursos",condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            # fin seleccionar alumno

            # obtener serial curso
            pkCurso = registros[0][0]
            # fin obtener serial curso


            # lista Salones
            SalonBD.mostrarLista(self)
            # fin lista Salones

            # seleccionar salon
            identificador = input("Ingrese el identificador del salon : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("salon", condicion)
            header = ['IdSalon', 'Nombre',
                      'Anio Escolar', 'IdentificadorSalon']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar salon

            # obtener serial salon
            pkSalon = registros[0][0]
            # fin obtener serial salon

            salon_curso = {
                "idSalon": pkSalon,
                "idCurso": pkCurso
            }

            if self.conexion.insertar_registro("salon_curso",salon_curso):
                print("Se ha asignado el curso")
                input("¿Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos", ex)

    def desasignarCurso(self):
        try:
            # listar cursos
            CursoBD.mostrarLista(self)
            # fin listar cursos

            # seleccionar alumno
            identificador = input("Ingrese el identificador del Curso : ")
            condicion = {"identificador":identificador}
            resultado = self.conexion.obtener_registros("cursos",condicion)
            header = ['IdCurso', 'identificadorcurso', 'nombre']
            registros = [list(registro.values()) for registro in resultado] # Lista de listas con los valores de los registros
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # print(resultado)
            # fin seleccionar alumno

            # obtener serial curso
            pkCurso = registros[0][0]
            # fin obtener serial curso


            # lista Salones
            SalonBD.mostrarLista(self)
            # fin lista Salones

            # seleccionar salon
            identificador = input("Ingrese el identificador del curso : ")
            condicion = {"identificador": identificador}
            resultado = self.conexion.obtener_registros("salon", condicion)
            header = ['IdSalon', 'Nombre',
                      'Anio Escolar', 'IdentificadorSalon']
            # Lista de listas con los valores de los registros
            registros = [list(registro.values()) for registro in resultado]
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
            # fin seleccionar salon

            # obtener serial salon
            pkSalon = registros[0][0]
            # fin obtener serial salon

            salon_curso = {
                "idSalon": pkSalon,
                "idCurso": pkCurso
            }

            if self.conexion.borrar_registro("salon_curso",salon_curso):
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
        identificador = input("Ingrese el identificador del Salon : ")
        condicion = {"identificador": identificador}
        resultado = self.conexion.obtener_registros("salon", condicion)
        header = ['IdSalon', 'Nombre',
                      'Anio Escolar', 'IdentificadorSalon']
        # Lista de listas con los valores de los registros
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar salon

        # obtener serial salon
        pkSalon = registros[0][0]
        # fin obtener serial salon

        # seleccionar salon
        condicion = {"idSalon": pkSalon}
        resultado = self.conexion.obtener_registros("salon_curso", condicion)
        header = ['id', 'idSalon', 'idCurso']
        # Lista de listas con los valores de los registros
        registros = [list(registro.values()) for registro in resultado]
        print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
        # fin seleccionar salon

        for registro in registros:
            pkCurso = registro[2]
            condicion = {"_id": pkCurso}
            resultado = self.conexion.obtener_registros("cursos", condicion)
            header = ['id', 'idCurso', 'idProfesor']
            registros = [list(registro.values()) for registro in resultado]

            print("Curso")
            print(tabulate(registros, headers=header, tablefmt='fancy_grid'))
