from clases import Profesores, Cursos, Salones
from conexion import Conexion
from utils import *

conexion = Conexion("mongodb://localhost:27017", "sv005618467")

def crearProfesor():
    identificador = input("Ingrese Identificador: ")
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingresa Edad: "))
    correo = input("Ingrese Correo: ")
    salones = list()
    opc = 1
    while(opc == 1):
        nombreSalon = input("Ingrese Nombre Salon: ")
        añoEscolar = int(input("Ingrese Año Escolar: "))
        bimestre = input("Ingrese Bimestre: ")
        salon = Salones(nombreSalon, añoEscolar, bimestre)
        salones.append(salon.__dict__)
        opc = int(input("Desea Ingresar otro salon?[1- Si, 2- No] "))
    cursos = list()
    opc2 = 1
    while(opc2 == 1):
        nombreCurso = input("Ingrese Nombre de Curso: ")
        curso = Cursos(nombreCurso)
        cursos.append(curso.__dict__)
        opc2 = int(input("Desea Ingresar otro Curso?[1- Si, 2- No] "))

    profesor = Profesores(identificador, nombre, edad, correo, salones, cursos)
    conexion.insertar_registro("Profesores", profesor.__dict__)

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
    conexion.actualizar_registros("Profesores", condicion, nuevoValor)

def actualizarCursos(identificador, campo):
    cursos = list()
    opc = 1
    while(opc == 1):
        nombre = input("Ingrese Nombre de Curso: ")
        curso = Cursos(nombre)
        cursos.append(curso.__dict__)
        opc = int(input("Desea Ingresar otro Curso?[1- Si, 2- No] "))
    
    condicion = {"identificador": identificador}
    nuevoValor = { "$set":{"cursos" : cursos}}
    conexion.actualizar_registro("Profesores", condicion, nuevoValor)

def actualizarCampo(identificador, campo):
    condicion = {"identificador": identificador}
    valor = input("Ingrese el nuevo valor: ")
    nuevoValor = { "$set":{campo: valor}}
    conexion.actualizar_registro("Profesores", condicion, nuevoValor)

def actualizarEdad(identificador, campo):
    condicion = {"identificador": identificador}
    valor = int(input("Ingrese el nuevo valor: "))
    nuevoValor = { "$set":{campo: valor}}
    conexion.actualizar_registro("Profesores", condicion, nuevoValor)

def actualizarProfesor():
    identificador = input("Ingrese el Identificador del Profesor que desea editar: ")
    campo = input("Ingrese campo que desea actualizar: ")
    condicion = {"identificador" : identificador}
    conexion.obtener_registros("Profesores", condicion)
    if(campo == "salones"):
        actualizarSalones(identificador, campo)
    elif(campo == "cursos"):
        actualizarCursos(identificador, campo)
    elif(campo == "edad"):
        actualizarEdad(identificador, campo)
    else:
        actualizarCampo(identificador, campo)

def asignarSalonesProf():
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

def eliminarSalonesProf():
    identificador = input("Ingrese Identificador del Alumno: ")
    nombre = input("Ingrese Nombre Salon: ")
    condicion = {"identificador": identificador}
    nuevoValor = { "$pull":{"salones" : {"nombre" : nombre}}}
    conexion.actualizar_registros("Profesores", condicion, nuevoValor)

def asignarCursos():
    identificador = input("Ingrese Identificador del Profesor: ")
    opc = 1
    while(opc == 1):
        nombre = input("Ingrese Nombre de Curso: ")
        curso = Cursos(nombre)
        condicion = {"identificador": identificador}
        nuevoValor = { "$push":{"cursos" : curso.__dict__}}
        conexion.actualizar_registro("Profesores", condicion, nuevoValor)
        opc = int(input("Desea Ingresar otro Curso?[1- Si, 2- No] "))

def eliminarCursos():
    identificador = input("Ingrese Identificador del Alumno: ")
    nombre = input("Ingrese Nombre: ")
    condicion = {"identificador": identificador}
    nuevoValor = { "$pull":{"cursos" : {"nombre" : nombre}}}
    conexion.actualizar_registros("Profesores", condicion, nuevoValor)

def buscarProfesor():
    identificador = input("Ingrese identificador: ")
    condicion = {"identificador" : identificador}
    res = conexion.obtener_registros("Profesores", condicion)
    print(res)

def eliminarProfesor():
    identificador = input("Ingrese el identificador del Profesor que desea Eliminar: ")
    condicion = {"identificador" : identificador}
    conexion.borrar_registros("Profesores", condicion)

def listarProfesores():
    profesores = conexion.listar_registros("Profesores")
    print(color.RED+"-------DATOS DE LOS PROFESORES------"+color.END)
    for profesor in profesores:
        print(color.GREEN+"Identificador: " +profesor['identificador']+color.END)
        print(f"Nombre: {profesor['nombre']}, Edad: {profesor['edad']}, Correo: {profesor['correo']}")
        print(color.CYAN+"Lista Salones:"+color.END)
        for salon in profesor['salones']:
            print(f"Nombre: {salon['nombre']}, Año Escolar: {salon['añoEscolar']}, Bimestre: {salon['bimestre']}")
        print(color.CYAN+"Lista Notas Bimestrales: "+color.END)
        for curso in profesor['cursos']:
            print(f"Nombre: {curso['nombre']}")
