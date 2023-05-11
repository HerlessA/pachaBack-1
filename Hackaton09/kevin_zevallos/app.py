from flask import Flask, request,render_template,redirect,url_for
from flask_orator import Orator, jsonify

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

db = Orator(app)
#MODELOS
class Alumno(db.Model):
    __fillable__ = ['id','nombre','edad','correo']
    __table__ = 'alumnos'
class Profesor(db.Model):
    __fillable__ = ['id','nombre','edad','correo']
    __table__ = 'profesores'

class Salon(db.Model):
    __fillable__ = ['nombre', 'año_escolar']
    __table__ = 'salones'
class Curso(db.Model):
    __fillable__ = ['nombre', 'profesor']
    __table__ = 'cursos'
#RUTAS

# Definir rutas de la API Alumnos
@app.route('/')
def index():
    return render_template('base.html')
    
@app.route('/alumnos/create',methods=['POST','GET'])
def create_alumno():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        correo = request.form['correo']
        alumno = Alumno.create(nombre= nombre,edad=edad,correo=correo)
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('alumnos/create-alumno.html')
    
@app.route('/alumnos/delete',methods=['POST','GET'])
def delete_alumno():
    if request.method == 'POST':
        id_alumno = request.form['id']
        alumno= Alumno.find(id_alumno)
        alumno.delete()
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('alumnos/delete-alumno.html')

@app.route('/alumnos/<int:id>',methods=['GET'])
def get_alumno(id):
    alumno = Alumno.find_or_fail(id)
    return jsonify(alumno)
@app.route('/alumnos',methods=['GET'])
def get_all_alumnos():
    alumnos = Alumno.all()
    return render_template('alumnos/alumnos.html',alumnos = alumnos)
@app.route('/alumnos/<int:id>',methods=['PATCH'])
def update_alumno(id):
    alumno = Alumno.find_or_fail(id)
    alumno.update(**request.get_json())
    return jsonify(alumno)
# Definir rutas de la API Profesores
@app.route('/profesores/create',methods=['POST','GET'])
def create_profesor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        correo = request.form['correo']
        profesor = Profesor.create(nombre= nombre,edad=edad,correo=correo)
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('profesores/create-profesor.html')
@app.route('/profesores/delete',methods=['POST','GET'])
def delete_profesor():
    if request.method == 'POST':
        id_profesor = request.form['id']
        profesor= Profesor.find(id_profesor)
        profesor.delete()
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('profesores/delete-profesor.html')
@app.route('/profesores/<int:id>',methods=['GET'])
def get_profesor(id):
    profesor = Profesor.find_or_fail(id)
    return jsonify(profesor)

@app.route('/profesores',methods=['GET'])
def get_all_profesores():
    profesores = Profesor.all()
    return render_template('profesores/profesores.html',profesores = profesores)

@app.route('/profesores/<int:id>',methods=['PATCH'])
def update_profesor(id):
    profesor = Profesor.find_or_fail(id)
    profesor.update(**request.get_json())
    return jsonify(profesor)
# Definir rutas de la API Cursos
@app.route('/cursos/create',methods=['POST','GET'])
def create_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        profesor = request.form['profesor']
        curso = Curso.create(nombre= nombre,profesor=profesor)
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('cursos/create-curso.html')
@app.route('/cursos/delete',methods=['POST','GET'])
def delete_curso():
    if request.method == 'POST':
        id_curso = request.form['id']
        curso= Curso.find(id_curso)
        curso.delete()
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('cursos/delete-curso.html')
@app.route('/cursos/<int:id>',methods=['GET'])
def get_curso(id):
    curso = Curso.find_or_fail(id)
    return jsonify(curso)

@app.route('/cursos',methods=['GET'])
def get_all_cursos():
    cursos = Curso.all()
    return render_template('cursos/cursos.html',cursos = cursos)

@app.route('/cursos/<int:id>',methods=['PATCH'])
def update_curso(id):
    curso = curso.find_or_fail(id)
    curso.update(**request.get_json())
    return jsonify(curso)
# Definir rutas de la API Salones
@app.route('/salones/create',methods=['POST','GET'])
def create_salon():
    if request.method == 'POST':
        nombre = request.form['nombre']
        año_escolar = request.form['año escolar']
        salon = Salon.create(nombre= nombre,año_escolar=año_escolar)
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('salones/create-salon.html')
@app.route('/salones/delete',methods=['POST','GET'])
def delete_salon():
    if request.method == 'POST':
        id_salon = request.form['id']
        salon= Salon.find(id_salon)
        salon.delete()
        return render_template('base.html')
    if request.method == 'GET':
        return render_template('salones/delete-salon.html')
@app.route('/salones/<int:id>',methods=['GET'])
def get_salon(id):
    salon = Salon.find_or_fail(id)
    return jsonify(salon)

@app.route('/salones',methods=['GET'])
def get_all_salones():
    salones = Salon.all()
    return render_template('salones/salones.html',salones = salones)

@app.route('/salones/<int:id>',methods=['PATCH'])
def update_salon(id):
    salon = salon.find_or_fail(id)
    salon.update(**request.get_json())
    return jsonify(salon)


if __name__ == '__main__':
    app.run(host="localhost",port=8000,debug=True)