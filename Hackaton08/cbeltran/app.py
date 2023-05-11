import os
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many

# Configuracion
DEBUG = True
ORATOR_DATABASES = {
    'default': 'SV70098291',
    'SV70098291': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'root',
        'database': 'SV70098291'
    }
}


app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


db = Orator(app)
if __name__ == '__main__':
    app.run()

#------------------------------------------------------MODELOS-----------------------------------------------------
class Alumno(db.Model):
    __fillable__ = ['nombre', 'email', 'dni', 'edad', 'email']

    @belongs_to
    def salon(self):
        return Salon

class Salon(db.Model):
    __fillable__ = ['nombre','anio_escolar']

    @has_many
    def alumno(self):
        return Alumno
    
class Docente(db.Model):
    __fillable__ = ['nombre', 'email', 'dni', 'edad', 'email']


class Curso(db.Model):
    __fillable__ = ['nombre']

#------------------------------------------------------RUTAS-----------------------------------------------------

#RUTAS DE ALUMNOS
@app.route('/alumnos', methods=['POST'])
def crear_alumno():
    alumno = Alumno.create(**request.get_json())

    return jsonify(alumno)

@app.route('/alumnos/<int:alumno_id>', methods=['GET'])
def listar_alumno(alumno_id):
    alumno = Alumno.find_or_fail(alumno_id)

    return jsonify(alumno)

@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    alumno = Alumno.all()

    return jsonify(alumno)

@app.route('/alumnos/<int:alumno_id>', methods=['PATCH'])
def actualizar_alumno(alumno_id):
    alumno = Alumno.find_or_fail(alumno_id)
    alumno.update(**request.get_json())

    return jsonify(alumno)

#RUTAS DE SALONES
@app.route('/salones', methods=['POST'])
def crear_salon():
    salon = Salon.create(**request.get_json())

    return jsonify(salon)

@app.route('/salones/<int:salon_id>', methods=['GET'])
def listar_salon(salon_id):
    salon = Salon.find_or_fail(salon_id)

    return jsonify(salon)

@app.route('/salones', methods=['GET'])
def listar_salones():
    salon = Salon.all()

    return jsonify(salon)

@app.route('/salones/<int:salon_id>', methods=['PATCH'])
def actualizar_salon(salon_id):
    salon = Salon.find_or_fail(salon_id)
    salon.update(**request.get_json())

    return jsonify(salon)

#RUTAS DE DOCENTES
@app.route('/docentes', methods=['POST'])
def crear_docente():
    docente = Docente.create(**request.get_json())

    return jsonify(docente)

@app.route('/docentes/<int:docente_id>', methods=['GET'])
def listar_docente(docente_id):
    docente = Docente.find_or_fail(docente_id)

    return jsonify(docente)

@app.route('/docentes', methods=['GET'])
def listar_docentes():
    docente = Docente.all()

    return jsonify(docente)

@app.route('/docentes/<int:docente_id>', methods=['PATCH'])
def actualizar_docente(docente_id):
    docente = Docente.find_or_fail(docente_id)
    docente.update(**request.get_json())

    return jsonify(docente)

#RUTAS DE CURSOS
@app.route('/cursos', methods=['POST'])
def crear_curso():
    curso = Curso.create(**request.get_json())

    return jsonify(curso)

@app.route('/cursos/<int:curso_id>', methods=['GET'])
def listar_curso(curso_id):
    curso = Curso.find_or_fail(curso_id)

    return jsonify(curso)

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    curso = Curso.all()

    return jsonify(curso)

@app.route('/cursos/<int:curso_id>', methods=['PATCH'])
def actualizar_curso(curso_id):
    curso = Curso.find_or_fail(curso_id)
    curso.update(**request.get_json())

    return jsonify(curso)