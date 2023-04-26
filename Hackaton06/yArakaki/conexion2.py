import psycopg2
import os
import time
from colorama import init, Fore, Back, Style


def SolicitudBaseDatos(solicitud):
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="pruebadb",
            user="postgres",
            password="Estudio8",
            port=5432,
        )

        cursor = conexion.cursor()
        sql = f" {solicitud}"
        cursor.execute(sql)
        conexion.commit()

    except Exception as error:
        print("Algo salio mal: ", error)

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()
        print("Conexion cerrada")


def ImprimirBaseDeDatos(tabla):
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="pruebadb",
            user="postgres",
            password="Estudio8",
            port=5432,
        )
        cursor = conexion.cursor()
        sql = f" SELECT * FROM {tabla}"
        cursor.execute(sql)
        conexion.commit()
        rows = cursor.fetchall()
        
        for row in rows:
            print("|".join(str(x) for x in row))
        
        print("Solictud exitosa")

                 

    except Exception as error:
        print("Algo salio mal: ", error)

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()
        print("Conexion cerrada")




def VerDatos():
    print("""¿Que datos desea verificar?
            1.- Lista de Alumnos
            2.- Lista de Profesores
            3.- Lista de Cursos
            4.- Lista de Salones
            5.- Lista de Notas
        """)
    eleccion = str(input(""))

    if eleccion == "1":
        ImprimirBaseDeDatos(tabla="alumnos")
    elif eleccion == "2":
        ImprimirBaseDeDatos(tabla="profesores")
    elif eleccion == "3":
        ImprimirBaseDeDatos(tabla="cursos")
    elif eleccion == "4":
        ImprimirBaseDeDatos(tabla="salones")
    elif eleccion == "5":
        ImprimirBaseDeDatos(tabla="notas")
    else:
        print(Fore.BLACK + Back.RED +
                  "¡Ingresa un valor correcto, por favor!" + Style.RESET_ALL)
        time.sleep(5)
        os.system("cls")

def AgregarDatos():
    print("""¿Que datos desea agregar?
            1.- Lista de Alumnos
            2.- Lista de Profesores
        """)
    eleccion = str(input(""))

    if eleccion == "1":
        ImprimirBaseDeDatos(tabla="alumnos")
    elif eleccion == "2":
        ImprimirBaseDeDatos(tabla="profesores")
    else:
        print(Fore.BLACK + Back.RED +
                  "¡Ingresa un valor correcto, por favor!" + Style.RESET_ALL)
        time.sleep(5)
        os.system("cls")

def Menu():

    while True:
        print("*" * 80)
        print(Fore.BLACK + Back.GREEN +
              "Bienvenido, escoge una opcion" + Style.RESET_ALL)
        print("""
            1.- Ver datos
            2.- Agregar Datos
            3.- Eliminar Datos
            4.- Modificar Datos
            5.- Salir
            """)
        print("*" * 80)
        opcion = str(input(""))

        if opcion == "1":
            os.system("cls")
            VerDatos()
        elif opcion == "2":
            os.system("cls")
            AgregarDatos()
        elif opcion == "3":
            os.system("cls")
            EliminarDatos()
        elif opcion == "4":
            os.system("cls")
            ModificarDatos()
        elif opcion == "5":
            print(Fore.BLACK + Back.GREEN +
              "¡Hasta pronto!" + Style.RESET_ALL)
            break
        else:
            print(Fore.BLACK + Back.RED +
                  "¡Ingresa un valor correcto, por favor!" + Style.RESET_ALL)
            time.sleep(5)
            os.system("cls")


if __name__ == "__main__":
    Menu()