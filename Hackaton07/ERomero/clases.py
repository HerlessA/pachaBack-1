import pymongo

cliente = pymongo.MongoClient("localhost", 27017)
db = cliente["a0973286"]

class Persona:
    def __init__(self, nombre, identificador, edad, correo):
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo

class Alumno(Persona):
    def insertar(self):
        db.alumnos.insert_one({
            "nombre": self.nombre,
            "identificador": self.identificador,
            "edad": self.edad,
            "correo": self.correo
        })

    def actualizar(self):
        db.alumnos.update_one(
            {"identificador": self.identificador},
            {"$set": {
                "nombre": self.nombre,
                "edad": self.edad,
                "correo": self.correo
            }}
        )

    def eliminar(self):
        db.alumnos.delete_one({"identificador": self.identificador})

    @staticmethod
    def seleccionar(identificador):
        resultado = db.alumnos.find_one({"identificador": identificador})
        if resultado is None:
            return None
        else:
            nombre = resultado["nombre"]
            identificador = resultado["identificador"]
            edad = resultado["edad"]
            correo = resultado["correo"]
            return Alumno(nombre, identificador, edad, correo)

class Salon:
    def __init__(self, nombre, anio_escolar):
        self.nombre = nombre
        self.anio_escolar = anio_escolar

    def insertar(self):
        db.salones.insert_one({
            "nombre": self.nombre,
            "anio_escolar": self.anio_escolar
        })

    def actualizar(self):
        db.salones.update_one(
            {"nombre": self.nombre},
            {"$set": {
                "anio_escolar": self.anio_escolar
            }}
        )

    def eliminar(self):
        db.salones.delete_one({"nombre": self.nombre})

    @staticmethod
    def seleccionar(nombre):
        resultado = db.salones.find_one({"nombre": nombre})
        if resultado is None:
            return None
        else:
            nombre = resultado["nombre"]
            anio_escolar = resultado["anio_escolar"]
            return Salon(nombre, anio_escolar)

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def insertar(self):
        db.cursos.insert_one({
            "nombre": self.nombre,
            "profesor": self.profesor.identificador
        })

    def actualizar(self):
        db.cursos.update_one(
            {"nombre": self.nombre},
            {"$set": {
                "profesor": self.profesor.identificador
            }}
        )

    def eliminar(self):
        db.cursos.delete_one({"nombre": self.nombre})

    @staticmethod
    def seleccionar(nombre):
        resultado = db.cursos.find_one({"nombre": nombre})
        if resultado is None:
            return None
        else:
            nombre = resultado["nombre"]
            profesor_id = resultado["profesor"]
            profesor = Profesor.seleccionar(profesor_id)
            return Curso(nombre, profesor)

    def buscar_profesor(self):
        return self.profesor.nombre



class Profesor(Persona):
    def __init__(self, nombre, profesor_id):
        self.nombre = nombre
        self.profesor_id = profesor_id

    def insertar(self):
        profesor = Profesor.seleccionar(self.profesor_id)
        db.cursos.insert_one({
            "nombre": self.nombre,
            "profesor": {
                "identificador": profesor.identificador,
                "nombre": profesor.nombre
            }
        })

    def actualizar(self):
        profesor = Profesor.seleccionar(self.profesor_id)
        db.cursos.update_one(
            {"nombre": self.nombre},
            {"$set": {
                "profesor": {
                    "identificador": profesor.identificador, 
                    "nombre": profesor.nombre
                }
            }}
        )

    def eliminar(self):
        db.cursos.delete_one({"nombre": self.nombre})

    @staticmethod
    def seleccionar(nombre):
        resultado = db.cursos.find_one({"nombre": nombre})
        if resultado is None:
            return None
        else:
            nombre = resultado["nombre"]
            profesor_id = resultado["profesor"]["identificador"]
            profesor = Profesor.seleccionar(profesor_id)
            return Curso(nombre, profesor)
