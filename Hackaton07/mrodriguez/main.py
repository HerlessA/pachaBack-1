import time
import tabulate
import os
from dotenv import load_dotenv
from conexion import Conexion
from utils import Menu, Color
from models.alumno import Alumno
from models.curso import Curso
from models.nota import Nota
from models.profesor import Profesor
from models.salon import Salon

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
conn = Conexion(MONGODB_URI, "SV73265099")


def menuSalon():
    try:
        opMenu = {
            "Crear salón": "1",
            "Mostrar salones": "2",
            "Eliminar salón": "3",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de salones", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break
            elif ansMenu == "1":
                list_alumnos = []
                list_cursos = []
                print(Color.BOLD + "INGRESA DATOS DEL SALON" + Color.END)
                id = int(input("ID N°: "))
                nombre = input("Nombre: ")
                periodo = input("Periodo: ")
                course = True
                while course:
                    print("")
                    print(f"¿Desea agregar cursos? (si/no)")
                    res = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if res.strip().lower() == "si":
                        print(Color.BOLD + "INGRESA DATOS DEL CURSO" + Color.END)
                        id_curso = int(input("ID N°: "))
                        nombre_curso = input("Nombre: ")
                        print("")
                        print(Color.BOLD + "INGRESA DATOS DEL PROFESOR" + Color.END)
                        id_profesor = int(input("ID N°: "))
                        nombre_profesor = input("Nombre: ")
                        dni_profesor = input("DNI: ")
                        edad_profesor = int(input("Edad: "))
                        correo_profesor = input("Correo: ")
                        dict_profesor = {
                            "id": id_profesor,
                            "nombre": nombre_profesor,
                            "dni": dni_profesor,
                            "edad": edad_profesor,
                            "correo": correo_profesor,
                        }
                        alumno = True
                        while alumno:
                            print("")
                            print(f"¿Desea agregar alumnos? (si/no)")
                            res = input(Color.YELLOW + "Respuesta: " + Color.END)
                            if res.strip().lower() == "si":
                                print("INGRESA DATOS DE ALUMNO")
                                id_alumno = int(input("ID N°: "))
                                nombre_alumno = input("Nombre: ")
                                dni_alumno = input("DNI: ")
                                edad_alumno = int(input("Edad: "))
                                correo_alumno = input("Correo: ")
                                dict_alumno = {
                                    "id": id_alumno,
                                    "nombre": nombre_alumno,
                                    "dni": dni_alumno,
                                    "edad": edad_alumno,
                                    "correo": correo_alumno,
                                    "notas": [],
                                }
                                list_alumnos.append(dict_alumno)
                            elif res.strip().lower() == "no":
                                break
                            else:
                                print(
                                    Color.RED + "❌Ingresa una opción válida" + Color.END
                                )
                        dict_curso = {
                            "id": id_curso,
                            "nombre": nombre_curso,
                            "profesor": dict_profesor,
                            "alumnos": list_alumnos,
                        }
                        list_cursos.append(dict_curso)
                        list_alumnos = []
                    elif res.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
                dict = Salon(id, nombre, periodo, list_cursos)
                list_cursos = []
                if conn.insertar_registro("salon", dict.__dict__):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print("")
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "2":
                res = conn.obtener_registros("salon", {})
                if res == []:
                    print(Color.BOLD + Color.YELLOW + f"⚠️  Data vacía.")
                    time.sleep(2)
                else:
                    print(res)
                    confirm = True
                    while confirm:
                        print("")
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "3":
                id = int(input("Ingresa ID del salón: "))
                res = conn.obtener_registros("salon", {"id": id})
                print(res)
                confirm = True
                while confirm:
                    print("")
                    print(f"¿Esta seguro de borrar los datos del salón? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conn.borrar_registro("salon", condition={"id": id}):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


def menuAlumnos():
    try:
        opMenu = {
            "Crear alumno": "1",
            "Mostrar alumnos": "2",
            "Editar alumno": "3",
            "Eliminar alumno": "4",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de alumnos", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break
            elif ansMenu == "1":
                print("INGRESA DATOS DEL ALUMNO")
                id = int(input("ID N°: "))
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                dict = Alumno(id, nombre, dni, edad, correo, [])
                if conn.insertar_registro("alumno", dict.__dict__):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "2":
                res = conn.obtener_registros("alumno", {})
                if res == []:
                    print(Color.BOLD + Color.YELLOW + f"⚠️  Data vacía.")
                    time.sleep(2)
                else:
                    header = res[0].keys()
                    rows = [x.values() for x in res]
                    print(tabulate.tabulate(rows, header, tablefmt="rst"))
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "3":
                id = int(input("Ingresa ID del alumno: "))
                res = conn.obtener_registros("alumno", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                print(Color.YELLOW + "Ingresa nueva información:" + Color.END)
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                newValues = {
                    "id": id,
                    "nombre": nombre,
                    "dni": dni,
                    "edad": edad,
                    "correo": correo,
                    "notas": [],
                }
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del alumno? (si/no)")
                    res = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if res.strip().lower() == "si":
                        if conn.actualizar_registro(
                            "alumno",
                            condition={"id": id},
                            newValues={"$set": newValues},
                        ):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif res.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
            elif ansMenu == "4":
                id = int(input("Ingresa ID del alumno: "))
                res = conn.obtener_registros("alumno", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del alumno? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conn.borrar_registro("alumno", condition={"id": id}):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


def menuProfesores():
    try:
        opMenu = {
            "Crear profesor": "1",
            "Mostrar profesor": "2",
            "Editar profesor": "3",
            "Eliminar profesor": "4",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de profesores", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break
            elif ansMenu == "1":
                print("INGRESA DATOS DEL PROFESOR")
                id = int(input("ID N°: "))
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                dict = Profesor(id, nombre, dni, edad, correo)
                if conn.insertar_registro("profesor", dict.__dict__):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "2":
                res = conn.obtener_registros("profesor", {})
                if res == []:
                    print(Color.BOLD + Color.YELLOW + f"⚠️  Data vacía.")
                    time.sleep(2)
                else:
                    header = res[0].keys()
                    rows = [x.values() for x in res]
                    print(tabulate.tabulate(rows, header, tablefmt="rst"))
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "3":
                id = int(input("Ingresa ID del profesor: "))
                res = conn.obtener_registros("profesor", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                print(Color.YELLOW + "Ingresa nueva información:" + Color.END)
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                newValues = {
                    "id": id,
                    "nombre": nombre,
                    "dni": dni,
                    "edad": edad,
                    "correo": correo,
                }
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del profesor? (si/no)")
                    res = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if res.strip().lower() == "si":
                        if conn.actualizar_registro(
                            "profesor",
                            condition={"id": id},
                            newValues={"$set": newValues},
                        ):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif res.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
            elif ansMenu == "4":
                id = int(input("Ingresa ID del profesor: "))
                res = conn.obtener_registros("profesor", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del profesor? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conn.borrar_registro("profesor", condition={"id": id}):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


def menuCursos():
    try:
        opMenu = {
            "Crear curso": "1",
            "Mostrar cursos": "2",
            "Editar curso": "3",
            "Eliminar curso": "4",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de cursos", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break
            elif ansMenu == "1":
                print("INGRESA DATOS DEL CURSO")
                id = int(input("ID N°: "))
                nombre = input("Nombre: ")
                dict = Curso(id, nombre, {}, [])
                if conn.insertar_registro("curso", dict.__dict__):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "2":
                res = conn.obtener_registros("curso", {})
                if res == []:
                    print(Color.BOLD + Color.YELLOW + f"⚠️  Data vacía.")
                    time.sleep(2)
                else:
                    header = res[0].keys()
                    rows = [x.values() for x in res]
                    print(tabulate.tabulate(rows, header, tablefmt="rst"))
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break
            elif ansMenu == "3":
                id = int(input("Ingresa ID del curso: "))
                res = conn.obtener_registros("curso", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                print(Color.YELLOW + "Ingresa nueva información:" + Color.END)
                nombre = input("Nombre: ")
                newValues = {"id": id, "nombre": nombre, "profesor": {}, "alumnos": []}
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del curso? (si/no)")
                    res = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if res.strip().lower() == "si":
                        if conn.actualizar_registro(
                            "curso",
                            condition={"id": id},
                            newValues={"$set": newValues},
                        ):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif res.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
            elif ansMenu == "4":
                id = int(input("Ingresa ID del curso: "))
                res = conn.obtener_registros("curso", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del curso? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conn.borrar_registro("curso", condition={"id": id}):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


try:
    opMenuPrincipal = {
        "Menu Salon": "1",
        "Menu Alumnos": "2",
        "Menu Profesores": "3",
        "Menu Cursos": "4",
        "Salir": "0",
    }
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.showMenu()
        if ansMenuPrincipal == "0":
            break
        elif ansMenuPrincipal == "1":
            menuSalon()
        elif ansMenuPrincipal == "2":
            menuAlumnos()
        elif ansMenuPrincipal == "3":
            menuProfesores()
        elif ansMenuPrincipal == "4":
            menuCursos()
except Exception as error:
    print(str(error))
