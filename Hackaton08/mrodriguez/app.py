from dotenv import load_dotenv
import os
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many


# Configuration
load_dotenv()
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

DEBUG = True
ORATOR_DATABASES = {
    "default": "twittor",
    "twittor": {
        "driver": "postgres",
        "host": "localhost",
        "user": "postgres",
        "password": POSTGRES_PASSWORD,
        "database": "SV73265099",
    },
}

# Creando Flask app
app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
# Inicializando Orator
db = Orator(app)


# Modelos
class Alumno(db.Model):
    __fillable__ = ["nombre", "dni", "edad", "email"]

    @belongs_to
    def salon(self):
        return Salone


class Profesore(db.Model):
    __fillable__ = ["nombre", "dni", "edad", "email"]

    @belongs_to_many
    def cursos(self):
        return Curso

    @belongs_to
    def salon(self):
        return Salone


class Curso(db.Model):
    __fillable__ = ["nombre", "profesor_id"]

    @belongs_to_many
    def profesores(self):
        return Profesore


class Salone(db.Model):
    __fillable__ = ["nombre", "periodo", "alumno_id", "profesor_id"]

    @has_many
    def alumnos(self):
        return Alumno

    @has_many
    def profesores(self):
        return Profesore


# Ruta ALUMNOS
@app.route("/alumnos", methods=["POST"])
def create_alumno():
    req = Alumno.create(**request.get_json())
    return jsonify(req)


@app.route("/alumnos", methods=["GET"])
def get_alumnos():
    req = Alumno.all()
    return jsonify(req)


@app.route("/alumnos/<int:alumno_id>", methods=["PATCH"])
def update_alumno(alumno_id):
    req = Alumno.find_or_fail(alumno_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/alumnos/<int:alumno_id>", methods=["DELETE"])
def delete_alumno(alumno_id):
    req = Alumno.find_or_fail(alumno_id)
    req.delete()
    return app.response_class("No Content", 204)


# Ruta PPROFESORES
@app.route("/profesores", methods=["POST"])
def create_profesor():
    req = Profesore.create(**request.get_json())
    return jsonify(req)


@app.route("/profesores", methods=["GET"])
def get_profesores():
    req = Profesore.all()
    return jsonify(req)


@app.route("/profesores/<int:profesor_id>", methods=["PATCH"])
def update_profesor(profesor_id):
    req = Profesore.find_or_fail(profesor_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/profesores/<int:profesor_id>", methods=["DELETE"])
def delete_profesor(profesor_id):
    req = Profesore.find_or_fail(profesor_id)
    req.delete()
    return app.response_class("No Content", 204)


# Ruta CURSOS
@app.route("/cursos", methods=["POST"])
def create_curso():
    req = Curso.create(**request.get_json())
    return jsonify(req)


@app.route("/cursos", methods=["GET"])
def get_cursos():
    req = Curso.all()
    return jsonify(req)


@app.route("/cursos/<int:curso_id>", methods=["PATCH"])
def update_curso(curso_id):
    req = Curso.find_or_fail(curso_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/cursos/<int:curso_id>", methods=["DELETE"])
def delete_curso(curso_id):
    req = Curso.find_or_fail(curso_id)
    req.delete()
    return app.response_class("No Content", 204)


# Ruta SALONES
@app.route("/salones", methods=["POST"])
def create_salon():
    req = Salone.create(**request.get_json())
    return jsonify(req)


@app.route("/salones", methods=["GET"])
def get_salones():
    req = Salone.all()
    return jsonify(req)


@app.route("/salones/<int:salon_id>", methods=["PATCH"])
def update_salon(salon_id):
    req = Salone.find_or_fail(salon_id)
    req.update(**request.get_json())
    return jsonify(req)


if __name__ == "__main__":
    app.run()
