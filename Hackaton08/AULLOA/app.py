from dotenv import load_dotenv
import os
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many



load_dotenv()
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

DEBUG = True
ORATOR_DATABASES = {
    "default": "postgres",
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "user": "postgres",
        "password": POSTGRES_PASSWORD,
        "database": "SV73969282",
    },
}


app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

db = Orator(app)



class Alumnos(db.Model):
    __fillable__ = ["nombre", "dni", "edad", "email"]

    @belongs_to
    def salon(self):
        return Salones


class Profesores(db.Model):
    __fillable__ = ["nombre", "dni", "edad", "email"]

    @belongs_to_many
    def cursos(self):
        return Cursos

    @belongs_to
    def salon(self):
        return Salones


class Cursos(db.Model):
    __fillable__ = ["nombre", "profesor_id"]

    @belongs_to_many
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


if __name__ == "__main__":
    app.run()