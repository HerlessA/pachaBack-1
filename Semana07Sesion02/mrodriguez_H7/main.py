import time
import tabulate
from conexion import Conexion
from utils import Menu, Color
from models.alumno import Alumno
from models.profesor import Profesor
from models.curso import Curso
from models.periodo import Periodo
from models.salon import Salon

# URI, DBname
conn = Conexion("mongodb://localhost:27017", "SV123")


# MENU ALUMNOS
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

            elif ansMenu == "1":  # Crear alumno
                print("INGRESA DATOS DEL ALUMNO")
                id = int(input("ID N°: "))
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                dict = Alumno(nombre, dni, edad, correo, id)
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

            elif ansMenu == "2":  # Mostrar alumnos
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

            elif ansMenu == "3":  # Editar alumno
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

            elif ansMenu == "4":  # "Eliminar alumno"
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


# MENU PROFESORES
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
                dict = Profesor(nombre, dni, edad, correo, id)
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


# MENU CURSOS
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
                id_profesor = input("ID del profesor: ")
                dict = Curso(id, nombre, id_profesor)
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
                id_profesor = input("ID del profesor: ")
                newValues = {
                    "id": id,
                    "nombre": nombre,
                    "id_profesor": id_profesor,
                }
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


# MENU PERIODOS
def menuPeriodos():
    try:
        opMenu = {
            "Crear periodo": "1",
            "Mostrar periodos": "2",
            "Editar periodo": "3",
            "Eliminar periodo": "4",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de periodos", opMenu)

        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":
                print("INGRESA DATOS DEL PERIODO")
                id = int(input("ID N°: "))
                nombre = input("Nombre: ")
                bimestre = int(input("N° de Bimestre: "))
                dict = Periodo(id, nombre, bimestre)
                if conn.insertar_registro("periodo", dict.__dict__):
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
                res = conn.obtener_registros("periodo", {})
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
                id = int(input("Ingresa ID del periodo: "))
                res = conn.obtener_registros("periodo", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))
                print(Color.YELLOW + "Ingresa nueva información:" + Color.END)
                nombre = input("Nombre: ")
                bimestre = int(input("N° de Bimestre: "))
                newValues = {
                    "id": id,
                    "nombre": nombre,
                    "bimestre": bimestre,
                }
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del periodo? (si/no)")
                    res = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if res.strip().lower() == "si":
                        if conn.actualizar_registro(
                            "periodo",
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
                id = int(input("Ingresa ID del periodo: "))
                res = conn.obtener_registros("periodo", {"id": id})
                header = res[0].keys()
                rows = [x.values() for x in res]
                print(tabulate.tabulate(rows, header, tablefmt="rst"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del periodo? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conn.borrar_registro("periodo", condition={"id": id}):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

    except Exception as error:
        print(str(error))


# MENU PRINCIPAL
try:
    opMenuPrincipal = {
        "Menu Alumnos": "1",
        "Menu Profesores": "2",
        "Menu Cursos": "3",
        "Menu Salon": "4",
        "Menu Periodos": "5",
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
            menuAlumnos()
        elif ansMenuPrincipal == "2":
            menuProfesores()
        elif ansMenuPrincipal == "3":
            menuCursos()
        elif ansMenuPrincipal == "4":
            print("Menu Salon")
        elif ansMenuPrincipal == "5":
            menuPeriodos()
except Exception as error:
    print(str(error))
