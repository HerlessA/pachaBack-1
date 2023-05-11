# Clases que representan las tablas en la base de datos aquí
from orator.orm import Model
from orator import DatabaseManager, Schema
import psycopg2
from orator import Model
from config import db

Model.set_connection_resolver(db)


class Salon(Model):
    __timestamps__ = False
    __fillable__ = ['nombre', 'capacidad']
    __table__ = 'salones'

class Alumno(Model):
    __table__ = 'alumnos'
    __fillable__ = ['nombre', 'apellido', 'correo']
    __timestamps__ = False

class Curso(Model):
    __table__ = 'cursos'
    __fillable__ = ['nombre', 'salon_id', 'profesor_id']
    __timestamps__ = False

class Nota(Model):
    __table__ = 'notas'
    __fillable__ = ['alumno_id', 'curso_id', 'nota']
    __timestamps__ = False

class Bimestre(Model):
    __table__ = 'bimestres'
    __fillable__ = ['numero', 'anio']
    __timestamps__ = False

class Profesor(Model):
    __table__ = 'profesores'
    __fillable__ = ['nombre', 'apellido', 'correo']
    __timestamps__ = False
