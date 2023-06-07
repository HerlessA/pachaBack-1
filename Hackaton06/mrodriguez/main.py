import time
from tabulate import tabulate
from conexion import Conexion
from utils import Menu, Color
from models.alumno import Alumno
from models.profesor import Profesor


conexion = Conexion()
lstAlumnos = []
lstprofesores = []
lstProfesores = []


def cargaInicial():
    query = "Select * from alumnos;"
    res = conexion.consultarBDD(query=query)
    for a in res:
        alumno = Alumno(a[0], a[1], a[2], a[3], a[4])
        lstAlumnos.append(alumno)

    query = "Select * from profesores;"
    res = conexion.consultarBDD(query=query)
    for p in res:
        profesor = Profesor(p[0], p[1], p[2], p[3], p[4])
        lstProfesores.append(profesor)


cargaInicial()


# MENU SALON
def menuSalones():
    try:
        opMenu = {
            "Crear salon": "1",
            "Mostrar salon": "2",
            "Buscar salon": "3",
            "Editar salon": "4",
            "Eliminar salon": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de salones", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear
                print("INGRESA DATOS DEL SALON")
                seccion = input("Sección: ")
                id_alumno = input("ID de alumno: ")
                id_periodo = input("ID de periodo: ")
                id_profesor = input("ID de profesor: ")
                query = f"""INSERT INTO salones(seccion, id_alumno, id_periodo, id_profesor) VALUES ('{seccion}',{id_alumno}, {id_periodo}, {id_profesor});"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar
                header = ["ID", "Sección", "IdAlumno", "IdPeriodo", "IdProfesor"]
                query = "SELECT * FROM salones;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar
                idSalon = int(input("Ingresa ID del salón: "))
                query = f"SELECT * FROM salones WHERE id = {idSalon};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Sección", "IdAlumno", "IdPeriodo", "IdProfesor"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar
                idSalon = int(input("Ingresa ID del salon: "))
                query = f"SELECT * FROM salones WHERE id = {idSalon};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Sección", "IdAlumno", "IdPeriodo", "IdProfesor"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                seccion = input("Sección: ")
                id_alumno = input("ID de alumno: ")
                id_periodo = input("ID de periodo: ")
                id_profesor = input("ID de profesor: ")
                query = f"""UPDATE salones SET seccion = '{seccion}',
                id_alumno = {id_alumno}, id_periodo = {id_periodo}, id_profesor = {id_profesor};"""
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del salon? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar
                idSalon = int(input("Ingresa ID del salon a borrar: "))
                query = f"SELECT * FROM salones WHERE id = {idSalon};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Sección", "IdAlumno", "IdPeriodo", "IdProfesor"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del salón? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM salones WHERE id = {idSalon};"""
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


# MENU ALUMNOS
def menuAlumnos():
    try:
        opMenu = {
            "Crear alumno": "1",
            "Mostrar alumno": "2",
            "Buscar alumno": "3",
            "Editar alumno": "4",
            "Eliminar alumno": "5",
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
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                query = f"""INSERT INTO alumnos(nombre, dni, edad, correo) VALUES ('{nombre}','{dni}',{edad},'{correo}');"""
                if conexion.ejecutarBDD(query):
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
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                query = "SELECT * FROM alumnos;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar alumno"
                idAlumno = int(input("Ingresa ID del alumno: "))
                query = f"SELECT * FROM alumnos WHERE id = {idAlumno};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar alumno
                idAlumno = int(input("Ingresa ID del alumno: "))
                query = f"SELECT * FROM alumnos WHERE id = {idAlumno};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                query = f"""UPDATE alumnos SET nombre = '{nombre}',
                dni = '{dni}', edad = {edad}, correo = '{correo}' WHERE id = {idAlumno};"""
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del alumno? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar alumno"
                idAlumno = int(input("Ingresa ID de alumno a borrar: "))
                query = f"SELECT * FROM alumnos WHERE id = {idAlumno};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del alumno? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM alumnos WHERE id = {idAlumno};"""
                        if conexion.ejecutarBDD(query):
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
            "Buscar profesor": "3",
            "Editar profesor": "4",
            "Eliminar profesor": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de profesores", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear profesor
                print("INGRESA DATOS DEL PROFESOR")
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                query = f"""INSERT INTO profesores(nombre, dni, edad, correo) VALUES ('{nombre}','{dni}',{edad},'{correo}');"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar profesores
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                query = "SELECT * FROM profesores;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar profesor"
                idProfesor = int(input("Ingresa ID del profesor: "))
                query = f"SELECT * FROM profesores WHERE id = {idProfesor};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar profesor
                idAlumno = int(input("Ingresa ID del profesor: "))
                query = f"SELECT * FROM profesores WHERE id = {idProfesor};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                nombre = input("Nombre: ")
                dni = input("DNI: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                query = f"""UPDATE profesores SET nombre = '{nombre}',
                dni = '{dni}', edad = {edad}, correo = '{correo}' WHERE id = {idProfesor};"""
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del profesor? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar PROFESOR"
                idProfesor = int(input("Ingresa ID de profesor a borrar: "))
                query = f"SELECT * FROM profesores WHERE id = {idProfesor};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre", "DNI", "Edad", "Correo"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del profesor? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f"""DELETE FROM profesores WHERE id = {idProfesor};"""
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


# MENU PERIODO ESCOLAR
def menuPeriodo():
    try:
        opMenu = {
            "Crear perido escolar": "1",
            "Mostrar perido escolar": "2",
            "Buscar perido escolar": "3",
            "Editar perido escolar": "4",
            "Eliminar perido escolar": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de perido escolar", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear
                print("INGRESA DATOS DEL PERIODO ESCOLAR")
                denominacion = input("Denominación: ")
                id_bimestre = input("ID de bimestre: ")
                query = f"""INSERT INTO periodos(denominacion, id_bimestre) VALUES ('{denominacion}',{id_bimestre});"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar
                header = ["ID", "Denominación", "IdBimestre"]
                query = "SELECT * FROM periodos;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar
                idPeriodo = int(input("Ingresa ID del periodo escolar: "))
                query = f"SELECT * FROM periodos WHERE id = {idPeriodo};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Denominación", "IdBimestre"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar
                idPeriodo = int(input("Ingresa ID del periodo escolar: "))
                query = f"SELECT * FROM periodos WHERE id = {idPeriodo};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Denominación", "IdBimestre"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                denominacion = input("Denominación: ")
                id_bimestre = input("Id del bimestre: ")
                query = f"""UPDATE periodos SET denominacion = '{denominacion}',
                id_bimestre = {id_bimestre};"""
                confirm = True
                while confirm:
                    print(
                        f"¿Esta seguro de actualizar los datos del periodo escolar? (si/no)"
                    )
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar
                idPeriodo = int(input("Ingresa ID del periodo escolar a borrar: "))
                query = f"SELECT * FROM periodos WHERE id = {idPeriodo};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Denominación", "IdBimestre"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(
                        f"¿Esta seguro de borrar los datos del periodo escolar? (si/no)"
                    )
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM periodos WHERE id = {idPeriodo};"""
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


# MENU BIMESTRES
def menuBimestres():
    try:
        opMenu = {
            "Crear bimestre escolar": "1",
            "Mostrar bimestre escolar": "2",
            "Buscar bimestre escolar": "3",
            "Editar bimestre escolar": "4",
            "Eliminar bimestre escolar": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de bimestres", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear
                print("INGRESA DATOS DEL BIMESTRE")
                nombre = input("Nombre: ")
                query = f"""INSERT INTO bimestres(nombre) VALUES ('{nombre}');"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar
                header = ["ID", "Nombre"]
                query = "SELECT * FROM bimestres;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar
                idBimestre = int(input("Ingresa ID del bimestre: "))
                query = f"SELECT * FROM bimestres WHERE id = {idBimestre};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar
                idBimestre = int(input("Ingresa ID del bimestre: "))
                query = f"SELECT * FROM bimestres WHERE id = {idBimestre};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                nombre = input("Nombre: ")
                query = f"""UPDATE bimestres SET nombre = '{nombre}';"""
                confirm = True
                while confirm:
                    print(
                        f"¿Esta seguro de actualizar los datos del periodo escolar? (si/no)"
                    )
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar
                idBimestre = int(input("Ingresa ID del Bimestre a borrar: "))
                query = f"SELECT * FROM bimestres WHERE id = {idBimestre};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del bimestre? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM bimestres WHERE id = {idBimestre};"""
                        if conexion.ejecutarBDD(query):
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
            "Buscar curso": "3",
            "Editar curso": "4",
            "Eliminar curso": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de cursos", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear
                print("INGRESA DATOS DEL CURSO")
                nombre = input("Nombre: ")
                query = f"""INSERT INTO cursos(nombre) VALUES ('{nombre}');"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar
                header = ["ID", "Nombre"]
                query = "SELECT * FROM cursos;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar
                idCurso = int(input("Ingresa ID del curso: "))
                query = f"SELECT * FROM cursos WHERE id = {idCurso};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar
                idCurso = int(input("Ingresa ID del curso: "))
                query = f"SELECT * FROM cursos WHERE id = {idCurso};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                nombre = input("Nombre: ")
                query = f"""UPDATE cursos SET nombre = '{nombre}';"""
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar los datos del curso? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar
                idCurso = int(input("Ingresa ID del Curso a borrar: "))
                query = f"SELECT * FROM cursos WHERE id = {idCurso};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nombre"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos del curso? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM cursos WHERE id = {idCurso};"""
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


# MENU CURSOS.PROFESORES
def menuCursosProfesores():
    try:
        opMenu = {
            "Crear": "1",
            "Mostrar": "2",
            "Buscar": "3",
            "Editar": "4",
            "Eliminar": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de cursos_profesores", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear
                print("INGRESA DATOS DEL CURSOS_PROFESORES")
                id_curso = input("ID del curso: ")
                id_profesor = input("ID del profesor: ")
                query = f"""INSERT INTO cursosprofesores(id_curso, id_profesor) VALUES ({id_curso}, {id_profesor});"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar
                header = ["ID", "IdCurso", "IdProfesor"]
                query = "SELECT * FROM cursosprofesores;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar
                idCP = int(input("Ingresa ID del curso_profesor: "))
                query = f"SELECT * FROM cursosprofesores WHERE id = {idCP};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "IdCurso", "IdProfesor"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar
                idCP = int(input("Ingresa ID del curso: "))
                query = f"SELECT * FROM cursosprofesores WHERE id = {idCP};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "IdCurso", "IdProfesor"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                id_curso = input("ID del curso: ")
                id_profesor = input("ID del profesor: ")
                query = f"""UPDATE cursosprofesores SET id_curso = {id_curso}, id_profesor = {id_profesor};"""
                confirm = True
                while confirm:
                    print(
                        f"¿Esta seguro de actualizar los datos del curso_profesor? (si/no)"
                    )
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar
                idCP = int(input("Ingresa ID del Curso_Profesor a borrar: "))
                query = f"SELECT * FROM cursosprofesores WHERE id = {idCP};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "IdCurso", "IdProfesor"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(
                        f"¿Esta seguro de borrar los datos del curso_profesor? (si/no)"
                    )
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM cursosprofesores WHERE id = {idCP};"""
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Eliminado." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)
    except Exception as error:
        print(str(error))


# MENU NOTAS
def menuNotas():
    try:
        opMenu = {
            "Crear nota": "1",
            "Mostrar nota": "2",
            "Buscar nota": "3",
            "Editar nota": "4",
            "Eliminar nota": "5",
            "Regresar a Menu Principal": "0",
        }
        showMenu = True
        ansMenu = ""
        menu = Menu("de notas", opMenu)
        while showMenu:
            ansMenu = menu.showMenu()
            if ansMenu == "0":
                break

            elif ansMenu == "1":  # Crear
                print("INGRESA DATOS DE NOTA")
                valor = input("Nota: ")
                id_alumno = input("ID de alumno: ")
                id_curso = input("ID de curso: ")
                id_periodo = input("ID del periodo: ")
                query = f"""INSERT INTO notas(valor, id_alumno, id_curso, id_periodo) VALUES ('{valor}',{id_alumno}, {id_curso}, {id_periodo});"""
                if conexion.ejecutarBDD(query):
                    print("")
                    print(Color.GREEN + "Datos creados correctamente.")
                    print("")
                    confirm = True
                    while confirm:
                        print(Color.YELLOW + "Presiona `enter` para continuar.")
                        resp = input()
                        if not resp == True:
                            break

            elif ansMenu == "2":  # Mostrar
                header = ["ID", "Nota", "IdAlumno", "IdCurso", "IdPeriodo"]
                query = "SELECT * FROM notas;"
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "3":  # "Buscar
                idNota = int(input("Ingresa ID de la nota: "))
                query = f"SELECT * FROM notas WHERE id = {idNota};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nota", "IdAlumno", "IdCurso", "IdPeriodo"]
                print("")
                print(Color.GREEN + "Resultado: " + Color.END)
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                confirm = True
                while confirm:
                    print(Color.YELLOW + "Presiona `enter` para continuar.")
                    resp = input()
                    if not resp == True:
                        break

            elif ansMenu == "4":  # Editar
                idNota = int(input("Ingresa ID de la Nota: "))
                query = f"SELECT * FROM notas WHERE id = {idNota};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nota", "IdAlumno", "IdCurso", "IdPeriodo"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))
                print(Color.YELLOW + "Ingresa nueva información: " + Color.END)
                valor = input("Nota: ")
                id_alumno = input("ID de alumno: ")
                id_curso = input("ID de curso: ")
                id_periodo = input("ID del periodo: ")
                query = f"""UPDATE notas SET valor = {valor}, id_alumno = {id_alumno}, id_curso = {id_curso}, id_periodo = {id_periodo};"""
                confirm = True
                while confirm:
                    print(f"¿Esta seguro de actualizar la nota? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        if conexion.ejecutarBDD(query):
                            print(Color.GREEN + f"✅ Datos actualizados." + Color.END)
                            time.sleep(1)
                            break
                    elif resp.strip().lower() == "no":
                        break
                    else:
                        print(Color.RED + "❌Ingresa una opción valida." + Color.END)

            elif ansMenu == "5":  # "Eliminar
                idNota = int(input("Ingresa ID de la NOTA: "))
                query = f"SELECT * FROM notas WHERE id = {idNota};"
                res = conexion.consultarBDD(query=query)
                header = ["ID", "Nota", "IdAlumno", "IdCurso", "IdPeriodo"]
                print(tabulate(res, headers=header, tablefmt="fancy_grid"))

                confirm = True
                while confirm:
                    print(f"¿Esta seguro de borrar los datos de la nota? (si/no)")
                    resp = input(Color.YELLOW + "Respuesta: " + Color.END)
                    if resp.strip().lower() == "si":
                        query = f""" DELETE FROM notas WHERE id = {idNota};"""
                        if conexion.ejecutarBDD(query):
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
        "Menu Salon": "1",
        "Menu Alumnos": "2",
        "Menu Profesores": "3",
        "Menu Periodos": "4",
        "Menu Bimestres": "5",
        "Menu Cursos": "6",
        "Menu CursosProfesor": "7",
        "Menu Notas": "8",
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
            menuSalones()
        elif ansMenuPrincipal == "2":
            menuAlumnos()
        elif ansMenuPrincipal == "3":
            menuProfesores()
        elif ansMenuPrincipal == "4":
            menuPeriodo()
        elif ansMenuPrincipal == "5":
            menuBimestres()
        elif ansMenuPrincipal == "6":
            menuCursos()
        elif ansMenuPrincipal == "7":
            menuCursosProfesores()
        elif ansMenuPrincipal == "8":
            menuNotas()
except Exception as error:
    print(str(error))
