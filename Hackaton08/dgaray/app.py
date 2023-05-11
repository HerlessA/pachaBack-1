from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many
from flask_swagger_ui import get_swaggerui_blueprint
import json

#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'school',
    'school': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'port': 5433,
        'password': '021087Mikeyla',
        'database': 'school'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = Orator(app)

#Modelos
class Alumno(db.Model):
    __fillable__ = ['nombre', 'identificador','edad','email']
    # __hidden__ = ['pivot']
    # @has_many
    # def salones(self):
    #     return Profesor
    
    # @belongs_to_many(
    #     'salones',
    #     'alumno_id', 'profesor_id',
    #     with_timestamps=True
    # )
    # def salones(self):
    #     return Alumno

    # @belongs_to_many(
    #     'salones',
    #     'alumno_id', 'profesor_id',
    #     with_timestamps=True
    # )
    # def salones(self):
    #     return Alumno

class Profesores(db.Model):
    __fillable__ = ['nombre', 'identificador','edad','email']

#Rutas
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



@app.route('/profesores', methods=['GET'])
def get_profesores():
    profesores = Profesores.all()
    return jsonify(profesores)

@app.route('/profesores/<int:profesor_id>', methods=['GET'])
def get_profesor(profesor_id):
    profesor = Profesores.find_or_fail(profesor_id)
    return jsonify(profesor)

@app.route('/profesores', methods=['POST'])
def create_profesor():
    profesor = Profesores.create(**request.get_json())
    return jsonify(profesor)

@app.route('/profesores/<int:profesor_id>', methods=['PATCH'])
def update_profesor(profesor_id):
    profesor = Profesores.find_or_fail(profesor_id)
    profesor.update(**request.get_json())
    return jsonify(profesor)

@app.route('/profesores/<int:profesor_id>', methods=['DELETE'])
def delete_profesor(profesor_id):
    profesor = Profesores.find_or_fail(profesor_id)
    profesor.delete()
    return app.response_class('No Content', 204)


if __name__ == '__main__':
    app.run()