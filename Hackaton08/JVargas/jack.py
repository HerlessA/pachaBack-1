from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Crear motor de base de datos
engine = create_engine('sqlite:///escuela.db', echo=True)

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear base de datos
Base = declarative_base()

# Definir clases
class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    identificador = Column(String, unique=True)
    edad = Column(Integer)
    correo = Column(String)

    salon_id = Column(Integer, ForeignKey('salones.id'))
    salon = relationship('Salon', back_populates='alumnos')
    notas = relationship('Nota', back_populates='alumno')

class Salon(Base):
    __tablename__ = 'salones'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    anio_escolar = Column(String)

    profesores = relationship('Profesor', back_populates='salon')
    cursos = relationship('Curso', back_populates='salon')
    alumnos = relationship('Alumno', back_populates='salon')

class Curso(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    profesor_id = Column(Integer, ForeignKey('profesores.id'))
    profesor = relationship('Profesor', back_populates='cursos')
    salon_id = Column(Integer, ForeignKey('salones.id'))
    salon = relationship('Salon', back_populates='cursos')
    notas = relationship('Nota', back_populates='curso')

class Profesor(Base):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    identificador = Column(String, unique=True)
    edad = Column(Integer)
    correo = Column(String)

    salon_id = Column(Integer, ForeignKey('salones.id'))
    salon = relationship('Salon', back_populates='profesores')
    cursos = relationship('Curso', back_populates='profesor')

class Nota(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True)
    bimestre = Column(Integer)
    nota = Column(Integer)

    alumno_id = Column(Integer, ForeignKey('alumnos.id'))
    alumno = relationship('Alumno', back_populates='notas')
    curso_id = Column(Integer, ForeignKey('cursos.id'))
    curso = relationship('Curso', back_populates='notas')

# Crear tablas
Base.metadata.create_all(engine)
