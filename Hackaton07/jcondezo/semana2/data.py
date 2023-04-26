from conexion import Conexion

class Periodo:
    def __init__(self, periodoId, nombre, anio, mes):
        self.periodoId = periodoId
        self.nombre =nombre
        self.anio = anio
        self.mes = mes

class Profesor:
    def __init__(self, profesorId, nombre, identificador, edad, correo, curso):
        self.profesorId = profesorId
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo
        self.curso = curso

class Curso:
    def __init__(self, cursoId, nombre):
        self.cursoId = cursoId
        self.nombre =nombre

class Notas:
    def __init__(self, nota1, nota2, nota3, nota4, nota5, nota6):
        self.nota1 =nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5
        self.nota6 = nota6

class Alumno:
    def __init__(self, alumnoId, nombre, identificador, edad, correo, notas):
        self.alumnoId = alumnoId
        self.nombre =nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo
        self.notas = notas

class Salon:
    def __init__(self, salonId, nombre, periodo, profesor, alumno):
        self.salonId = salonId
        self.nombre = nombre
        self.periodo =periodo
        self.profesor = profesor
        self.alumno = alumno



# conn = Conexion("mongodb://localhost:27017", "Colegio")
# periodo=Periodo(1,"2023-A","2023","1")
# conn.insertar_registro("Periodo",periodo.__dict__)
# periodo=Periodo(2,"2023-B","2023","2")
# conn.insertar_registro("Periodo",periodo.__dict__)
