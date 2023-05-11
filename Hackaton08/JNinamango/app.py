from flask import Flask, request
from flask_orator import Orator, jsonify
from flask_cors import CORS, cross_origin
import json
from clases import Menu


#from modelos import User


DEBUG = True
ORATOR_DATABASES = {
    'default': 'twitor',
    'twitor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'warstrategoC123',
        'database': 'twitor'
    }
}


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = Orator(app)
    
class User(db.Model):
    __fillable__ = ['name', 'mail']
class Alumno(db.Model):
    __fillable__ = ['nombre', 'edad', 'correo','notas', 'id_salon']
class Curso(db.Model):
    __fillable__ = ['nombre', 'id_profesor']
class Profesor(db.Model):
    __fillable__ = ['nombre', 'edad', 'correo', 'id_salon']
class Salon(db.Model):
    __fillable__ = ['nombre', 'fecha']


@app.route("/")
def index():
    return "Hola mundo"

#http POST http://127.0.0.1:5000/users name= bro email = bro@gmail.com

########################################################################RUTAS DE ALUMNOS
@app.route('/api/alumnos/create/', methods = ['POST'])
def create_Alumno():

    req = request.get_json()
    user = Alumno.create(req)

    # {
    #     "nombre" : "nombre1",
    #     "edad": 1,
    #     "correo": "asdas@gmail.com",
    #     "notas": 10, 
    #     "id_salon": 2
    # }

    return jsonify(user)


@app.route('/api/alumnos/getall', methods = ['GET'])
def get_Alumnos():
    req = Alumno.all()
    print(req)
    return req.to_json()

@app.route('/api/alumnos/get/<int:usuario_id>', methods = ['GET'])
def get_Alumno(usuario_id):
    req = Alumno.find_or_fail(usuario_id)
    return req.to_json()

@app.route('/api/alumnos/update/<int:usuario_id>', methods = ['POST'])
def update_Alumno(usuario_id):
    req = Alumno.find_or_fail(usuario_id)
    req.update(request.get_json())
    return req.to_json()

@app.route('/api/alumnos/delete/<int:usuario_id>', methods = ['POST'])
def delete_Alumno(usuario_id):
    req = Alumno.find_or_fail(usuario_id)
    req.delete()
    return req.to_json()

#################################################################RUTAS DE PROFESORES
@app.route('/api/profesores/create/', methods = ['POST'])
def create_profesores():

    req = request.get_json()
    user = Profesor.create(req)

    # {
    #     "nombre" : "profesor1",
    #     "edad": 1,
    #     "correo": "asdas@gmail.com",
    #     "id_salon": 2
    # }

    return jsonify(user)


@app.route('/api/profesores/getall', methods = ['GET'])
def get_profesores():
    req = Profesor.all()
    print(req)
    return req.to_json()

@app.route('/api/profesores/get/<int:usuario_id>', methods = ['GET'])
def get_profesor(usuario_id):
    req = Profesor.find_or_fail(usuario_id)
    return req.to_json()

@app.route('/api/profesores/update/<int:usuario_id>', methods = ['POST'])
def update_profesores(usuario_id):
    req = Profesor.find_or_fail(usuario_id)
    req.update(request.get_json())
    return req.to_json()

@app.route('/api/profesores/delete/<int:usuario_id>', methods = ['POST'])
def delete_profesores(usuario_id):
    req = Profesor.find_or_fail(usuario_id)
    req.delete()
    return req.to_json()




############################################################################RUTAS DE SALONES
@app.route('/api/profesores/create/', methods = ['POST'])
def create_Salon():

    req = request.get_json()
    user = Salon.create(req)

    # {
    #     "nombre" : "salon1",
    #     "fecha": "2002/12/4",
    # }

    return jsonify(user)


@app.route('/api/salones/getall', methods = ['GET'])
def get_Salones():
    req = Salon.all()
    print(req)
    return req.to_json()

@app.route('/api/salones/get/<int:usuario_id>', methods = ['GET'])
def get_Salon(usuario_id):
    req = Salon.find_or_fail(usuario_id)
    return req.to_json()

@app.route('/api/salones/update/<int:usuario_id>', methods = ['POST'])
def update_Salon(usuario_id):
    req = Salon.find_or_fail(usuario_id)
    req.update(request.get_json())
    return req.to_json()

@app.route('/api/salones/delete/<int:usuario_id>', methods = ['POST'])
def delete_Salon(usuario_id):
    req = Salon.find_or_fail(usuario_id)
    req.delete()
    return req.to_json()



############################################################################RUTAS DE CURSO
@app.route('/api/cursos/create/', methods = ['POST'])
def create_Curso():

    req = request.get_json()
    user = Curso.create(req)

    # {
    #     "nombre" : "curso1",
    #     "id_profesor": 1,
    # }

    return jsonify(user)


@app.route('/api/cursos/getall', methods = ['GET'])
def get_Cursos():
    req = Curso.all()
    print(req)
    return req.to_json()

@app.route('/api/cursos/get/<int:usuario_id>', methods = ['GET'])
def get_Curso(usuario_id):
    req = Curso.find_or_fail(usuario_id)
    return req.to_json()

@app.route('/api/cursos/update/<int:usuario_id>', methods = ['POST'])
def update_Curso(usuario_id):
    req = Curso.find_or_fail(usuario_id)
    req.update(request.get_json())
    return req.to_json()

@app.route('/api/cursos/delete/<int:usuario_id>', methods = ['POST'])
def delete_Curso(usuario_id):
    req = Curso.find_or_fail(usuario_id)
    req.delete()
    return req.to_json()


if __name__ == '__main__':
    app.run()

