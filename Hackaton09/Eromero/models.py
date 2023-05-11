from orator import Model
from orator.orm import belongs_to, has_many
from orator import DatabaseManager, Schema
import psycopg2
from orator import Model
from config import db

Model.set_connection_resolver(db)

class Alumno(Model):
    __fillable__ = ['nombre', 'apellido', 'correo', 'password', 'salon_id']
    __table__ = 'alumnos'

    @belongs_to
    def salon(self):
        return Salon

    @has_many
    def notas(self):
        return Nota

class Profesor(Model):
    __fillable__ = ['nombre', 'apellido', 'correo', 'password', 'salon_id']
    __table__ = 'profesores'

    @belongs_to
    def salon(self):
        return Salon

    @has_many
    def notas(self):
        return Nota

class Salon(Model):
    __fillable__ = ['nombre']
    __table__ = 'salones'

    @has_many
    def alumnos(self):
        return Alumno

    @has_many
    def profesores(self):
        return Profesor

    @has_many
    def cursos(self):
        return Curso

class Curso(Model):
    __fillable__ = ['nombre', 'salon_id']
    __table__ = 'cursos'

    @belongs_to
    def salon(self):
        return Salon

    @has_many
    def notas(self):
        return Nota

class Bimestre(Model):
    __fillable__ = ['nombre', 'descripcion', 'anio_escolar']
    __table__ = 'bimestres'
    
    @has_many
    def notas(self):
        return Nota

class Nota(Model):
    __table__ = 'notas'

    @belongs_to
    def alumno(self):
        return Alumno

    @belongs_to
    def profesor(self):
        return Profesor

    @belongs_to
    def bimestre(self):
        return Bimestre

    @belongs_to
    def curso(self):
        return Curso

def authenticate_user(email, password):
    alumno = Alumno.where('correo', email).where('password', password).first()
    if alumno:
        return alumno

    profesor = Profesor.where('correo', email).where('password', password).first()
    if profesor:
        return profesor

    return None
