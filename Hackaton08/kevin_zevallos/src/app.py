from flask import Flask, request,render_template
from flask_orator import Orator, jsonify
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
        'password': 'admin',
        'database': 'colegio'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
SWAGGER_URL = '/swagger'
API_URL = 'http://localhost:8000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))


db = Orator(app)
#MODELOS
class Alumno(db.Model):
    __fillable__ = ['id','nombre','edad','correo']
    __table__ = 'alumnos'
class Profesor(db.Model):
    __fillable__ = ['id','nombre','edad','email']
    __table__ = 'profesores'

class Salon(db.Model):
    __fillable__ = ['nombre', 'año_escolar']
    __table__ = 'salones'
class Curso(db.Model):
    __fillable__ = ['nombre', 'profesor']
    __table__ = 'cursos'
#RUTAS

# Definir rutas de la API Alumnos
@app.route('/alumnos',methods=['POST'])
def create_alumno():
    alumno = Alumno.create(**request.get_json())
    return jsonify(alumno)
@app.route('/alumnos/<int:id>',methods=['GET'])
def get_alumno(id):
    alumno = Alumno.find_or_fail(id)
    return jsonify(alumno)
@app.route('/alumnos',methods=['GET'])
def get_all_alumnos():
    alumnos = Alumno.all()
    return jsonify(alumnos)
@app.route('/alumnos/<int:id>',methods=['PATCH'])
def update_alumno(id):
    alumno = Alumno.find_or_fail(id)
    alumno.update(**request.get_json())
    return jsonify(alumno)
# Definir rutas de la API Profesores
@app.route('/profesores',methods=['POST'])
def create_profesor():
    profesor = Profesor.create(**request.get_json())
    return jsonify(profesor)

@app.route('/profesores/<int:id>',methods=['GET'])
def get_profesor(id):
    profesor = Profesor.find_or_fail(id)
    return jsonify(profesor)

@app.route('/profesores',methods=['GET'])
def get_all_profesores():
    profesores = Profesor.all()
    return jsonify(profesores)

@app.route('/profesores/<int:id>',methods=['PATCH'])
def update_profesor(id):
    profesor = Profesor.find_or_fail(id)
    profesor.update(**request.get_json())
    return jsonify(profesor)
# Definir rutas de la API Cursos
@app.route('/cursos',methods=['POST'])
def create_curso():
    curso = Curso.create(**request.get_json())
    return jsonify(curso)

@app.route('/cursos/<int:id>',methods=['GET'])
def get_curso(id):
    curso = Curso.find_or_fail(id)
    return jsonify(curso)

@app.route('/cursos',methods=['GET'])
def get_all_cursos():
    cursos = Curso.all()
    return jsonify(cursos)

@app.route('/profesores/<int:id>',methods=['PATCH'])
def update_curso(id):
    curso = curso.find_or_fail(id)
    curso.update(**request.get_json())
    return jsonify(curso)
# Definir rutas de la API Salones
@app.route('/salones',methods=['POST'])
def create_salon():
    salon = Salon.create(**request.get_json())
    return jsonify(salon)

@app.route('/salones/<int:id>',methods=['GET'])
def get_salon(id):
    salon = Salon.find_or_fail(id)
    return jsonify(salon)

@app.route('/salones',methods=['GET'])
def get_all_salones():
    salones = Salon.all()
    return jsonify(salones)

@app.route('/salones/<int:id>',methods=['PATCH'])
def update_salon(id):
    salon = salon.find_or_fail(id)
    salon.update(**request.get_json())
    return jsonify(salon)


if __name__ == '__main__':
    app.run(host="localhost",port=8000,debug=True)