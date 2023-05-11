from clases import Alumnos, NotasBimestrales, Salones
from conexion import Conexion
from utils import *

conexion = Conexion("mongodb://localhost:27017", "sv005618467")

def crearAlumno():
    identificador = input("Ingrese Identificador: ")
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingresa Edad: "))
    correo = input("Ingrese Correo: ")
    salonesList = list()
    opc = 1
    while(opc == 1):
        nombreSalon = input("Ingrese Nombre Salon: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        salones = Salones(nombreSalon, añoEscolar, bimestre)
        salonesList.append(salones.__dict__)
        opc = int(input("Desea Ingresar otro salon?[1- Si, 2- No] "))
    notasBimestrales = list()
    opc = 1
    while(opc == 1):
        nota = input("Ingrese Nota: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        notaBimestral = NotasBimestrales(nota, añoEscolar, bimestre)
        notasBimestrales.append(notaBimestral.__dict__)
        opc = int(input("Desea Ingresar otra nota?[1- Si, 2- No] "))
    alumno = Alumnos(identificador, nombre, edad, correo, salonesList, notasBimestrales)
    conexion.insertar_registro("Alumnos", alumno.__dict__)

def actualizarSalones(identificador, campo):
    salones = list()
    opc = 1
    while(opc == 1):
        nombre = input("Ingrese Nombre Salon: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        salon = Salones(nombre, añoEscolar, bimestre)
        salones.append(salon.__dict__)
        opc = int(input("Desea Ingresar otro salon?[1- Si, 2- No] "))
    condicion = {"identificador": identificador}
    nuevoValor = { "$set":{"salones" : salones}}
    conexion.actualizar_registros("Alumnos", condicion, nuevoValor)

def actualizarNotas(identificador, campo):
    cursos = list()
    opc = 1
    while(opc == 1):
        nota = input("Ingrese Nota: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        notaBimestral = NotasBimestrales(nota, añoEscolar, bimestre)
        notasBimestrales.append(notaBimestral.__dict__)
        opc = int(input("Desea Ingresar otra nota?[1- Si, 2- No] "))
    condicion = {"identificador": identificador}
    nuevoValor = { "$set":{"cursos" : cursos}}
    conexion.actualizar_registro("Alumnos", condicion, nuevoValor)

def actualizarCampo(identificador, campo):
    condicion = {"identificador": identificador}
    valor = input("Ingrese el nuevo valor: ")
    nuevoValor = { "$set":{campo: valor}}
    conexion.actualizar_registro("Alumnos", condicion, nuevoValor)

def actualizarEdad(identificador, campo):
    condicion = {"identificador": identificador}
    valor = int(input("Ingrese el nuevo valor: "))
    nuevoValor = { "$set":{campo: valor}}
    conexion.actualizar_registro("Alumnos", condicion, nuevoValor)

def actualizarAlumno():
    identificador = input("Ingrese el Identificador del Alumno que desea editar: ")
    campo = input("Ingrese campo que desea actualizar: ")
    condicion = {"identificador" : identificador}
    conexion.obtener_registros("Alumnos", condicion)
    if(campo == "salones"):
        actualizarSalones(identificador, campo)
    elif(campo == "notas"):
        campo = "notasBimestrales"
        actualizarCursos(identificador, campo)
    elif(campo == "edad"):
        actualizarEdad(identificador, campo)
    else:
        actualizarCampo(identificador, campo)

def asignarSalonesAl():
    identificador = input("Ingrese Identificador del Profesor: ")
    opc = 1
    while(opc == 1):
        nombre = input("Ingrese Nombre Salon: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        salones = Salones(nombre, añoEscolar, bimestre)
        condicion = {"identificador": identificador}
        nuevoValor = { "$push":{"salones" : salones.__dict__}}
        opc = int(input("Desea Ingresar otro salon?[1- Si, 2- No] "))
        conexion.actualizar_registros("Profesores", condicion, nuevoValor)

def eliminarSalonesAl():
    identificador = input("Ingrese Identificador del Alumno: ")
    nombre = input("Ingrese Nombre Salon: ")
    condicion = {"identificador": identificador}
    nuevoValor = { "$pull":{"salones" : {"nombre" : nombre}}}
    conexion.actualizar_registros("Alumnos", condicion, nuevoValor)

def asignarNotas():
    identificador = input("Ingrese Identificador del Profesor: ")
    opc = 1
    while(opc == 1):
        nota = input("Ingrese Nota: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        notaBimestral = NotasBimestrales(nota, añoEscolar, bimestre)
        condicion = {"identificador": identificador}
        nuevoValor = { "$push":{"notasBimestrales" : notaBimestral.__dict__}}
        conexion.actualizar_registro("Profesores", condicion, nuevoValor)
        opc = int(input("Desea Ingresar otro Curso?[1- Si, 2- No] "))

def eliminarNotas():
    identificador = input("Ingrese Identificador del Alumno: ")
    nota = input("Ingrese Nota: ")
    bimestre = input("Ingrese Bimestre: ")
    condicion = {"identificador": identificador}
    nuevoValor = { "$pull":{"notasBimestrales" : {"nota" : nota, "bimestre": bimestre}}}
    conexion.actualizar_registros("Alumnos", condicion, nuevoValor)

def buscarAlumno():
    identificador = input("Ingrese identificador del Alumno que desea Mostrar: ")
    condicion = {"identificador" : identificador}
    res = conexion.obtener_registros("Alumnos", condicion)
    print(res)

def eliminarAlumno():
    identificador = input("Ingrese el identificador del Alumno que desea Eliminar: ")
    condicion = {"identificador" : identificador}
    conexion.borrar_registros("Alumnos", condicion)

def listarAlumnos():
    alumnos = conexion.listar_registros("Alumnos")
    print(color.RED+"-------DATOS DE LOS ALUMNOS------"+color.END)
    for alumno in alumnos:
        print(color.GREEN+"Identificador: " +alumno['identificador']+color.END)
        print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Correo: {alumno['correo']}")
        print(color.CYAN+"Lista Salones:"+color.END)
        for salon in alumno['salones']:
            print(f"Nombre: {salon['nombre']}, Año Escolar: {salon['añoEscolar']}, Bimestre: {salon['bimestre']}")
        print(color.CYAN+"Lista Notas Bimestrales: "+color.END)
        for nota in alumno['notasBimestrales']:
            print(f"Nota: {nota['nota']}, Año Escolar: {nota['añoEscolar']}, Bimestre: {nota['bimestre']}")
        print("")