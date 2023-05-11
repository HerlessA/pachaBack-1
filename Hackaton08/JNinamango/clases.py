import os
import time

class Alumno:
    def __init__(self, _id, nombre_alumno, edad_alumno, correo_alumno, notas_alumno, id_salon):
        self._id = _id
        self.nombre = nombre_alumno
        self.edad = edad_alumno
        self.correo = correo_alumno
        self.notas = notas_alumno
        self.id_salon = id_salon

class Salon:
    def __init__(self,  _id, nombre_salon, anio_salon):
        self._id = _id
        self.nombre = nombre_salon
        self.anio = anio_salon

class Profesor:
    def __init__(self, _id, nombre_profe, edad_profe, correo_profe,id_salon):
        self._id = _id
        self.nombre = nombre_profe
        self.edad = edad_profe
        self.correo = correo_profe
        self.id_salon = id_salon

class Curso:
    def __init__(self, _id, nombre_curso, id_profesor):
        self._id = _id
        self.nombre = nombre_curso
        self.id_profesor = id_profesor


class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("\n")
            print("::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.nombreMenu.upper()+"::::::::::::::::::::")          
            print("\n")

            for (key, value) in self.listaOpciones.items():
                print(key+" → "+value)

            print("\n")
            ans = input("Por favor, ingrese su opción: ")
            print("\n")

            if(ans.upper() == "0"):
                print("Hasta, pronto")
                break

            b = 0

            for (key, value) in self.listaOpciones.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False
            else:
                print("Opción no valida, escoja una opción valida")
                time.sleep(1)

        return ans             


    def limpiarPantalla(self):
        def clear():
               #return os.system('cls')
           return os.system('clear')
        clear()   
        
        # os.system('cls')

class TemplateObject:

    Lista_alumnos = list()

    def __init__(self, curso, profesor,salon, alumnos):
        self.curso = curso.__dict__
        self.profesor = profesor.__dict__
        self.salon = salon.__dict__

        for alumno in alumnos:
            self.Lista_alumnos.append(alumno.__dict__)

        self.alumnos = self.Lista_alumnos

# class DataBase:
#     def __init__(self, MONGO_URI, MONGO_TIME_FUERA, Mongo_BASE_DATOS):
        # self.cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeOutMS = MONGO_TIME_FUERA)#generamos cliente
        # self.baseDatos = self.cliente[Mongo_BASE_DATOS]
        # self.collectionCursos = self.baseDatos["cursos"]
        # self.collectionAlumnos = self.baseDatos["alumnos"]
        # self.collectionProfesores = self.baseDatos["profesores"]
        # self.collectionSalones = self.baseDatos["salones"]


    # def createTestValues(self):
    #     #datos iniciales para crear la database

    #     salon1 = Salon(1,"salon1","2020-1-5")
    #     salon2 =  Salon(2,"salon2","2019-1-5")
    #     salon3 =  Salon(3,"salon3","2015-1-5")

    #     alumno1 = Alumno(1,"alum1", 19, "alum1@gmail.com",[10,10,10],1)
    #     alumno2 = Alumno(2,"alum2", 20, "alum2@gmail.com",[10,10,10],2)
    #     alumno3 = Alumno(3,"alum3", 21, "alum3@gmail.com",[10,10,10],3)
    #     alumno4 = Alumno(4,"alum4", 21, "alum4@gmail.com",[10,10,10],1)
    #     alumno5 = Alumno(5,"alum5", 21, "alum5@gmail.com",[10,10,10],2)
    #     alumno6 = Alumno(6,"alum6", 21, "alum6@gmail.com",[10,10,10],3)

        
    #     prof1 = Profesor(1,"prof1", 49, "prof1@gmail.com",1)
    #     prof2 = Profesor(2,"prof2", 50, "prof2@gmail.com",2)
    #     prof3 = Profesor(3,"prof3", 51, "prof3@gmail.com",3)

    #     curso1 = Curso(1,"curso1",1)
    #     curso2 = Curso(2,"curso2",2)
    #     curso3 = Curso(3,"curso3",3)


    #     self.collectionSalones.insert_many([salon1.__dict__, salon2.__dict__, salon3.__dict__])
    #     self.collectionProfesores.insert_many([prof1.__dict__, prof2.__dict__, prof3.__dict__])
    #     self.collectionAlumnos.insert_many([alumno1.__dict__, alumno2.__dict__, alumno3.__dict__, alumno4.__dict__, alumno5.__dict__, alumno6.__dict__])
    #     self.collectionCursos.insert_many([curso1.__dict__, curso2.__dict__, curso3.__dict__])

        
