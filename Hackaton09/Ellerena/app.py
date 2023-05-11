from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many
from flask_sqlalchemy import SQLAlchemy
import db
import os

from forms import SignupForm, LoginForm, AlumnoForm
from models import users, get_user, User, Alumnos, Cursos, Salon, Profesor

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = Orator(app)
if __name__ == '__main__':
    app.run()


posts = []
alumnos = []
Clases = []
profesores = []
salones = []

@app.route("/")
def index():
    return render_template("index.html", alumnos=alumnos)


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


ORATOR_DATABASES = {
    'default': 'tarea08',
    'tarea08': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': '123',
        'database': 'tarea08'
    }
}


@app.route("/admin/alumnos/", methods=['GET', 'POST'], defaults={'id_alumno': None})
@app.route("/admin/alumnos/<int:id_alumno>/", methods=['GET', 'POST'])
@login_required
def post_form(id_alumno):
    form = AlumnoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        correo = form.correo.data
        identificador = form.identificador.data

        alumno = {'nombre': nombre, 'edad': edad, 'identificador': identificador, 'correo' : correo}
        alumnos.append(alumno)

        return redirect(url_for('index'))
    return render_template("admin/alumno_form.html", form=form)


@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


class Alumnos(db.Model):
    __fillable__ = ["nombre", "dni", "edad", "email"]

    @belongs_to
    def salon(self):
        return Salones


class Profesores(db.Model):
    __fillable__ = ["nombre", "dni", "edad", "email"]

   
    def cursos(self):
        return Cursos

    @belongs_to
    def salon(self):
        return Salones


class Cursos(db.Model):
    __fillable__ = ["nombre", "profesor_id"]

    
    def profesores(self):
        return Profesores


class Salones(db.Model):
    __fillable__ = ["nombre", "periodo", "alumno_id", "profesor_id"]

    @has_many
    def alumnos(self):
        return Alumnos

    @has_many
    def profesores(self):
        return Profesores


#alumnos
@app.route("/alumnos", methods=["POST"])
def create_alumno():
    req = Alumnos.create(**request.get_json())
    return jsonify(req)


@app.route("/alumnos", methods=["GET"])
def get_alumnos():
    req = Alumnos.all()
    return jsonify(req)


@app.route("/alumnos/<int:alumno_id>", methods=["PATCH"])
def update_alumno(alumno_id):
    req = Alumnos.find_or_fail(alumno_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/alumnos/<int:alumno_id>", methods=["DELETE"])
def delete_alumno(alumno_id):
    req = Alumnos.find_or_fail(alumno_id)
    req.delete()
    return app.response_class("No Content", 204)


#profesores
@app.route("/profesores", methods=["POST"])
def create_profesor():
    req = Profesores.create(**request.get_json())
    return jsonify(req)


@app.route("/profesores", methods=["GET"])
def get_profesores():
    req = Profesores.all()
    return jsonify(req)


@app.route("/profesores/<int:profesor_id>", methods=["PATCH"])
def update_profesor(profesor_id):
    req = Profesores.find_or_fail(profesor_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/profesores/<int:profesor_id>", methods=["DELETE"])
def delete_profesor(profesor_id):
    req = Profesores.find_or_fail(profesor_id)
    req.delete()
    return app.response_class("No Content", 204)


#cursos
@app.route("/cursos", methods=["POST"])
def create_curso():
    req = Cursos.create(**request.get_json())
    return jsonify(req)


@app.route("/cursos", methods=["GET"])
def get_cursos():
    req = Cursos.all()
    return jsonify(req)


@app.route("/cursos/<int:curso_id>", methods=["PATCH"])
def update_curso(curso_id):
    req = Cursos.find_or_fail(curso_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/cursos/<int:curso_id>", methods=["DELETE"])
def delete_curso(curso_id):
    req = Cursos.find_or_fail(curso_id)
    req.delete()
    return app.response_class("No Content", 204)


#salones
@app.route("/salones", methods=["POST"])
def create_salon():
    req = Salones.create(**request.get_json())
    return jsonify(req)


@app.route("/salones", methods=["GET"])
def get_salones():
    req = Salones.all()
    return jsonify(req)


@app.route("/salones/<int:salon_id>", methods=["PATCH"])
def update_salon(salon_id):
    req = Salones.find_or_fail(salon_id)
    req.update(**request.get_json())
    return jsonify(req)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)