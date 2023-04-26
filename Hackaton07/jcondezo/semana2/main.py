from conexion import Conexion
from utils import Menu
from data import *

try:
    opMenuPrincipal = {"Mostrar Datos": "1", "Crear Datos": "2","Editar Datos": "3","Borrar Datos":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)

    conn = Conexion("mongodb://localhost:27017", "Colegio")

    while showHome:
        ansMenuPrincipal = menuPrincipal.show()

        menuSecundario = ""
        opMenuSec = {"Alumno": "1", "Profesor": "2","Curso":"3","Salon": "4","Salir": "0"}
        menuSec = Menu("Secundario", opMenuSec)
        # ansMenuSec = menuSec.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            ansMenuSec = menuSec.show()
            if(ansMenuSec == "1"):
                id = int(input("Ingrese código del alumno: "))
                condicion = { 'alumnoId': id }
                print(conn.obtener_registros("Alumno", condicion))

            if(ansMenuSec == "2"):
                id = int(input("Ingrese código del profesor: "))
                condicion = { 'profesorId': id }
                print(conn.obtener_registros("Profesor",condicion))

            if(ansMenuSec == "3"):
                id = int(input("Ingrese nombre del curso: "))
                condicion = { 'cursoId': id }
                print(conn.obtener_registros("Curso",condicion))

            if(ansMenuSec == "4"):
                id = int(input("Ingrese nombre del salon: "))
                condicion = { 'salonId': id }
                print(conn.obtener_registros("Salon",condicion))

            input("Desea continuar??: ")

        if(ansMenuPrincipal == "2"):
            ansMenuSec = menuSec.show()
            if(ansMenuSec == "1"):
                id = int(input("Ingrese código del alumno: "))
                nombre = input("Ingrese su nombre: ")
                dni = input("Ingrese su dni: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo: ")

                n1 = input("Ingrese su nota1: ")
                n2 = input("Ingrese su nota2: ")
                n3 = input("Ingrese su nota3: ")
                n4 = input("Ingrese su nota4: ")
                n5 = input("Ingrese su nota5: ")
                n6 = input("Ingrese su nota6: ")

                notas= Notas(n1,n2,n3,n4,n5,n6)
                alumn = Alumno(id, nombre, dni, edad, correo, notas=notas.__dict__)
                conn.insertar_registro("Alumno",alumn.__dict__)

            if(ansMenuSec == "2"):
                id = int(input("Ingrese código del docente: "))
                nombre = input("Ingrese su nombre: ")
                dni = input("Ingrese su dni: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo: ")

                idCurso = int(input("Ingrese su codigo del Curso: "))
                condicion = { 'cursoId': idCurso }
                dat1 = conn.obtener_registros("Curso", condicion)

                doc = Profesor(id, nombre, dni, edad, correo, curso=dat1)
                conn.insertar_registro("Profesor", doc.__dict__)

            if(ansMenuSec == "3"):
                id = int(input("Ingrese código del curso: "))
                nombre = input("Ingrese nombre del curso: ")

                cur = Curso(id, nombre)
                conn.insertar_registro("Curso", cur.__dict__)

            if(ansMenuSec == "4"):
                id = int(input("Ingrese código del Salon: "))
                nombre = input("Ingrese nombre del Salon: ")

                idPeriodo = int(input("Ingrese código de Periodo: "))
                condicion = { 'periodoId': idPeriodo }
                d1 = conn.obtener_registros("Periodo",condicion)

                idProf = int(input("Ingrese código del Profesor: "))
                condicion1 = { 'profesorId': idProf }
                d2 = conn.obtener_registros("Profesor", condicion1)

                idAlumno = int(input("Ingrese código de Alumno: "))
                condicion2 = { 'alumnoId': idAlumno }
                d3 = conn.obtener_registros("Alumno",condicion2)

                salon = Salon(id, nombre, periodo=d1, profesor=d2, alumno=d3)

                conn.insertar_registro("Salon", salon.__dict__)

            input("Desea continuar??: ")

        if(ansMenuPrincipal == "3"):
            ansMenuSec = menuSec.show()
            if(ansMenuSec == "1"):
                id = int(input("Ingrese código del alumno: "))
                condicion = { 'alumnoId': id }
                data = conn.obtener_registros("Alumno", condicion)
                if data:
                    print(data[0]['nombre'])
                    nombre = input("Ingrese el nuevo nombre del alumno: ")
                    valor = { "$set": { 'nombre': nombre } }
                    respuesta = conn.actualizar_registro("Alumno", condicion, valor)
                    if respuesta:
                        print("Se modifico el registro!!!")
                    else:
                        print("Ocurrio un error al modificar registro.")
                else:
                    print('No existe el código..')

                input("Desea continuar??: ")

            if(ansMenuSec == "2"):
                id = int(input("Ingrese código del profesor: "))
                condicion = { 'profesorId': id }
                data = conn.obtener_registros("Profesor", condicion)
                if data:
                    print(data[0]['curso'])
                    cod = int(input("Ingrese código del curso: "))
                    dat1 = conn.obtener_registros("Curso", { 'cursoId': cod })
                    valor = { "$set": { 'curso': dat1 } }
                    respuesta = conn.actualizar_registro("Profesor", condicion, valor)
                    if respuesta:
                        print("Se modifico el registro!!!")
                    else:
                        print("Ocurrio un error al modificar registro.")
                else:
                    print('No existe el código..')

                input("Desea continuar??: ")

            if(ansMenuSec == "3"):
                id = int(input("Ingrese código del curso: "))
                condicion = { 'cursoId': id }
                data = conn.obtener_registros("Curso", condicion)
                if data:
                    print(data[0]['nombre'])
                    nombre = input("Ingrese el nuevo nombre del curso: ")
                    valor = { "$set": { 'nombre': nombre } }
                    respuesta = conn.actualizar_registro("Curso", condicion, valor)
                    if respuesta:
                        print("Se modifico el registro!!!")
                    else:
                        print("Ocurrio un error al modificar registro.")
                else:
                    print('No existe el código..')

                input("Desea continuar??: ")

            if(ansMenuSec == "4"):
                id = int(input("Ingrese código del salon: "))
                condicion = { 'salonId': id }
                data = conn.obtener_registros("Salon", condicion)
                if data:
                    print(data[0]['profesor'][0]['curso'])
                    cod = int(input("Ingrese código del curso: "))
                    dat1 = conn.obtener_registros("Curso", { 'cursoId': cod })
                    valor = { "$set": { 'profesor': [{'curso': dat1}] } }
                    respuesta = conn.actualizar_registro("Salon", condicion, valor)
                    if respuesta:
                        print("Se modifico el registro!!!")
                    else:
                        print("Ocurrio un error al modificar registro.")
                else:
                    print("No existe el código.")

                input("Desea continuar??: ")

        if(ansMenuPrincipal == "4"):
            ansMenuSec = menuSec.show()
            if(ansMenuSec == "1"):
                id = int(input("Ingrese código del alumno: "))
                condicion = { 'alumnoId': id }
                respuesta = conn.borrar_registros("Alumno",condicion)

            if(ansMenuSec == "2"):
                id = int(input("Ingrese código del profesor: "))
                condicion = { 'profesorId': id }
                respuesta = conn.borrar_registros("Profesor",condicion)

            if(ansMenuSec == "3"):
                id = int(input("Ingrese código del curso: "))
                condicion = { 'cursoId': id }
                respuesta = conn.borrar_registros("Curso",condicion)

            if(ansMenuSec == "4"):
                id = int(input("Ingrese código del salon: "))
                condicion = { 'salonId': id }
                respuesta = conn.borrar_registros("Salon",condicion)

            if(respuesta):
                print(f"Se elimino el registro correctamente!!!")
            else:
                print(f"No se Elimino")
            input("Desea continuar??: ")


except Exception as error:
    print(str(error))