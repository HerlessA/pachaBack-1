from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many

import json

#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': '123',
        'database': 'colegio'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


# Initializing Orator
db = Orator(app)

class Alumno(db.Model):
    __fillable__ = ['nombre', 'identificador', 'edad', 'correo']

class Profesor(db.Model):
    __fillable__ = ['nombre', 'identificador', 'edad', 'correo', ]

    @belongs_to
    def curso(self):
        return Curso

class Curso(db.Model):
    __fillable__ = ['nombre']



#RUTAS
# --------------------- ALUMNOS -----------------------------
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumno.all()
    return jsonify(alumnos)

@app.route('/alumnos/<int:alumno_id>', methods=['GET'])
def get_alumno(alumno_id):
    alumno = Alumno.find_or_fail(alumno_id)
    return jsonify(alumno)

@app.route('/alumnos', methods=['POST'])
def create_alumno():
    alumno = Alumno.create(**request.get_json())
    return jsonify(alumno)

@app.route('/alumnos/<int:alumno_id>', methods=['PATCH'])
def update_alumno(alumno_id):
    alumno = Alumno.find_or_fail(alumno_id)
    alumno.update(**request.get_json())
    return jsonify(alumno)

@app.route('/alumnos/<int:alumno_id>', methods=['DELETE'])
def delete_alumno(alumno_id):
    alumno = Alumno.find_or_fail(alumno_id)
    alumno.delete()
    return app.response_class('No Content', 204)



# --------------------- PROFESOR -----------------------------
@app.route('/profesor', methods=['GET'])
def get_profesors():
    profesor = Profesor.all()
    return jsonify(profesor)

@app.route('/profesor/<int:profesor_id>', methods=['GET'])
def get_profesor(profesor_id):
    profesor = Profesor.find_or_fail(profesor_id)
    return jsonify(profesor)

@app.route('/profesor', methods=['POST'])
def create_profesor():
    profesor = Profesor.create(**request.get_json())
    return jsonify(profesor)

@app.route('/profesor/<int:profesor_id>', methods=['PATCH'])
def update_profesor(profesor_id):
    profesor = Profesor.find_or_fail(profesor_id)
    profesor.update(**request.get_json())
    return jsonify(profesor)

@app.route('/profesor/<int:profesor_id>', methods=['DELETE'])
def delete_profesor(profesor_id):
    profesor = Profesor.find_or_fail(profesor_id)
    profesor.delete()
    return app.response_class('No Content', 204)


# --------------------- CURSOS -----------------------------
@app.route('/curso', methods=['GET'])
def get_cursos():
    curso = Curso.all()
    return jsonify(curso)

@app.route('/curso/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    curso = Curso.find_or_fail(curso_id)
    return jsonify(curso)

@app.route('/curso', methods=['POST'])
def create_curso():
    curso = Curso.create(**request.get_json())
    return jsonify(curso)

@app.route('/curso/<int:curso_id>', methods=['PATCH'])
def update_curso(curso_id):
    curso = Curso.find_or_fail(curso_id)
    curso.update(**request.get_json())
    return jsonify(curso)

@app.route('/curso/<int:curso_id>', methods=['DELETE'])
def delete_curso(curso_id):
    curso = Curso.find_or_fail(curso_id)
    curso.delete()
    return app.response_class('No Content', 204)





if __name__ == '__main__':
    app.run()