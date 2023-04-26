import os
from dotenv import load_dotenv
from conexion import Conexion
from models.alumno import Alumno
from models.curso import Curso
from models.nota import Nota
from models.profesor import Profesor
from models.salon import Salon


notas = list()
nota1 = Nota(18, 1)
nota2 = Nota(16, 2)
nota3 = Nota(20, 3)
nota4 = Nota(14, 4)
notas.append(nota1.__dict__)
notas.append(nota2.__dict__)
notas.append(nota3.__dict__)

alumnos = list()
alumno1 = Alumno(
    1,
    "Mari R",
    "73732020",
    20,
    "mari@gm.com",
    notas=notas,
)
alumno2 = Alumno(
    2,
    "Alicia Pérez",
    "27732027",
    25,
    "alicia@gmail.com",
    notas=notas,
)
alumno3 = Alumno(
    3,
    "Pedro Rámos",
    "85732025",
    28,
    "pedro@gmail.com",
    notas=notas,
)
alumnos.append(alumno1.__dict__)
alumnos.append(alumno2.__dict__)
alumnos.append(alumno3.__dict__)

profesor1 = Profesor(
    1,
    "Roberto Pineda",
    "50731828",
    38,
    "roberto@abcd.com",
)
profesor2 = Profesor(
    2,
    "Luis Martínez",
    "40731817",
    35,
    "luis@abcd.com",
)

cursos = list()
curso1 = Curso(1, "Álgebra", profesor=profesor1.__dict__, alumnos=alumnos)
curso2 = Curso(2, "Química", profesor=profesor2.__dict__, alumnos=alumnos)
cursos.append(curso1.__dict__)
cursos.append(curso2.__dict__)

salon = Salon(
    100,
    "A",
    "2023",
    cursos=cursos,
)

print(f"{salon.__dict__}")

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
conn = Conexion(MONGODB_URI, "SV73265099")
conn.insertar_registro("salon", salon.__dict__)
