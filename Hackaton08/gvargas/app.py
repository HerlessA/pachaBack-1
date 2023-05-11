import os
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many

#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'Colegio',
    'Colegio': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'Schadenfreude20',
        'database': 'Colegio'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Initializing Orator
db = Orator(app)

#Modelos

class Alumno(db.Model):
    __fillable__ = ['name','email', 'edad', 'identificador','notas']

class Profesores(db.Model):
    __fillable__ = ['name', 'email', 'edad', 'identificador']

class Curso(db.Model):
    __fillable__ = ['name', 'profesor']

class Salon(db.Model):
    __fillable__ = ['name', 'anhoescolar']

#Rutas
@app.route('/Alumnos', methods=['POST'])
def create_Alumno():
    alumno = Alumno.create(**request.get_json())
    return jsonify(alumno)

@app.route('/Alumnos/<int:alumno_id>', methods=['GET'])
def get_alumno(alumno_id):
    alumno = Alumno.find(alumno_id)

    return jsonify(alumno)

@app.route('/Alumnos', methods=['GET'])
def get_all_alumnos():
    alumno = Alumno.all()
    return jsonify(alumno)

@app.route('/Alumnos/<int:alumno_id>', methods=['PATCH'])
def update_alumno(alumno_id):
    alumno = Alumno.find_or_fail(alumno_id)
    alumno.update(**request.get_json())
    return jsonify(alumno)

@app.route('/Profesores', methods=['POST'])
def create_profesor():
    profesor = Profesores.create(**request.get_json())
    return jsonify(profesor)

@app.route('/Profesores/<int:alumno_id>', methods=['GET'])
def get_profesor(profesor_id):
    profesor = Profesores.find(profesor_id)

    return jsonify(profesor)

@app.route('/Profesores', methods=['GET'])
def get_all_profesores():
    profesor = Profesores.all()
    return jsonify(profesor)

@app.route('/Profesores/<int:profesor_id>', methods=['PATCH'])
def update_profesor(profesor_id):
    profesor = Profesores.find_or_fail(profesor_id)
    profesor.update(**request.get_json())
    return jsonify(profesor)

@app.route('/Curso', methods=['POST'])
def create_curso():
    curso = Curso.create(**request.get_json())
    return jsonify(curso)

@app.route('/Curso/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    curso = Curso.find(curso_id)

    return jsonify(curso)

@app.route('/Curso', methods=['GET'])
def get_all_cursos():
    curso = Curso.all()
    return jsonify(curso)

@app.route('/Curso/<int:curso_id>', methods=['PATCH'])
def update_curso(curso_id):
    curso = Curso.find_or_fail(curso_id)
    curso.update(**request.get_json())
    return jsonify(curso)

@app.route('/Salon', methods=['POST'])
def create_salon():
    salon = Salon.create(**request.get_json())
    return jsonify(salon)

@app.route('/Salon/<int:salon_id>', methods=['GET'])
def get_salon(salon_id):
    salon = Salon.find(salon_id)

    return jsonify(salon)

@app.route('/Salon', methods=['GET'])
def get_all_salon():
    salon = Salon.all()
    return jsonify(salon)

@app.route('/Salon/<int:salon_id>', methods=['PATCH'])
def update_salon(salon_id):
    salon = Salon.find_or_fail(salon_id)
    salon.update(**request.get_json())
    return jsonify(salon)

if __name__ == '__main__':
    app.run()
