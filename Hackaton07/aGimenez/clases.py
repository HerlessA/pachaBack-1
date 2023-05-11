class Persona: 
    def __init__(self, identificador, nombre, edad, correo):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

class Alumnos(Persona):
    def __init__(self, identificador, nombre, edad, correo, salones, notasBimestrales):
        super().__init__(identificador,nombre, edad, correo)
        # self.IdAlumno = IdAlumno
        self.salones = salones
        self.notasBimestrales = notasBimestrales


class Profesores(Persona):
    def __init__(self, identificador, nombre, edad, correo, salones, cursos):
        super().__init__(identificador, nombre, edad, correo)
        self.salones = salones
        self.cursos = cursos

class Salones:
    def __init__(self, nombre, añoEscolar, bimestre):
        #self.IdSalon = IdSalon
        self.nombre = nombre
        self.añoEscolar = añoEscolar
        self.bimestre = bimestre

class Cursos:
    def __init__(self, nombre):
        self.nombre = nombre

class NotasBimestrales:
    def __init__(self, nota,  añoEscolar, bimestre):
        self.nota = nota
        self.añoEscolar = añoEscolar
        self.bimestre = bimestre