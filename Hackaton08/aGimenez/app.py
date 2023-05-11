from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many
from flask_swagger_ui import get_swaggerui_blueprint
import json

#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'root0709',
        'database': 'sv005618467'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = Orator(app)

class Alumnos(db.Model):
    __fillable__ = ['nombre', 'identAlumno','edad','email']
    __table__ = 'alumnos'

    @has_many
    def salones(self):
        return Salones

class Profesores(db.Model):
    __fillable__ = ['nombre', 'identProfesor', 'edad', 'email']
    __table__ = 'profesores'

    @has_many
    def salones(self):
        return Salones
    @has_many
    def cursos(self):
        return Cursos

class Salones(db.Model):
    __fillable__ = ['nombre', 'año escolar']
    __table__ = 'salones'
    def alumnos(self):
        return Alumnos
    @belongs_to_many
    def profesores(self):
        return Profesores

class Cursos(db.Model):
    __fillable__ = ['nombre', 'profesorId']
    __table__ = 'cursos'
    @belongs_to_many
    def profesor(self):
        return Profesores

# Rutas Alumnos
@app.route('/alumnos', methods=['POST'])
def create_alumno():
    alumno = Alumnos.create(**request.get_json())
    return jsonify(alumno)

@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumnos.all()
    return jsonify(alumnos)

@app.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno(id):
    alumno = Alumnos.find_or_fail(id)
    return jsonify(alumno)

@app.route('/alumnos/<int:id>', methods=['PATCH'])
def update_alumno(id):
    alumno = Alumnos.find_or_fail(id)
    alumno.update(**request.get_json())
    return jsonify(alumno)

# Rutas Profesores
@app.route('/profesores', methods=['POST'])
def create_profesor():
    profesor = Profesores.create(**request.get_json())
    return jsonify(profesor)

@app.route('/profesores', methods=['GET'])
def get_profesores():
    profesores = Profesores.all()
    return jsonify(profesores)

@app.route('/profesores/<int:id>', methods=['GET'])
def get_profesor(id):
    profesor = Profesores.find_or_fail(id)
    return jsonify(profesor)

@app.route('/profesores/<int:id>', methods=['PATCH'])
def update_profesor(id):
    profesor = Profesores.find_or_fail(id)
    profesor.update(**request.get_json())
    return jsonify(profesor)

# Rutas Cursos
@app.route('/cursos', methods=['POST'])
def create_curso():
    curso = Cursos.create(**request.get_json())
    return jsonify(curso)

@app.route('/cursos', methods=['GET'])
def get_cursos():
    cursos = Cursos.all()
    return jsonify(cursos)

@app.route('/profesores/<int:profesor_id>/cursos', methods=['GET'])
def get_profesor_curso(profesor_id):
    profesor = Profesores.find_or_fail(profesor_id)
    return jsonify(profesor.cursos)


@app.route('/cursos/<int:id>', methods=['PATCH'])
def update_curso(id):
    curso = Cursos.find_or_fail(id)
    curso.update(**request.get_json())
    return jsonify(curso)

@app.route("/cursos/<int:id>", methods=["DELETE"])
def delete_curso(id):
    curso = Cursos.find_or_fail(id)
    curso.delete()
    return app.response_class("No Content", 204)

# Rutas Salones
@app.route("/salones", methods=["POST"])
def create_salon():
    salon = Salones.create(**request.get_json())
    return jsonify(salon)

@app.route("/salones", methods=["GET"])
def get_salones():
    salon = Salones.all()
    return jsonify(salon)

@app.route('/salones/<int:id>', methods=['GET'])
def get_salon(id):
    salon = Salones.find_or_fail(id)
    return jsonify(salon)

@app.route("/salones/<int:id>", methods=["PATCH"])
def update_salon(id):
    salon = Salones.find_or_fail(id)
    salon.update(**request.get_json())
    return jsonify(salon)

@app.route("/salones/<int:id>", methods=["DELETE"])
def delete_salon(id):
    salon = Salones.find_or_fail(id)
    salon.delete()
    return app.response_class("No Content", 204)

if __name__ == '__main__':
    app.run()