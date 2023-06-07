from dotenv import load_dotenv
import os
from flask import Flask, request
from psycopg2 import connect
from flask_orator import Orator
from flask_cors import CORS, cross_origin

load_dotenv()
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

ORATOR_DATABASES = {
    "default": "prueba",
    "prueba": {
        "driver": "postgres",
        "host": "localhost",
        "user": "postgres",
        "password": POSTGRES_PASSWORD,
        "database": "practice",
    },
}

app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

db = Orator(app)


class Usuarios(db.Model):
    __fillable__ = ["name", "email", "password"]


@app.get("/")
def funcionPrincipal():
    return "Servidor activo"


@app.get("/api/obtenerUsuarios")
def obternerUsuarios():
    users = Usuarios.all()
    return users.to_json()


@app.get("/api/encontrarUsuario/<int:usuario_id>")
def encontrarUsuario(usuario_id):
    req = Usuarios.find_or_fail(usuario_id)
    return req.to_json()


@app.post("/api/crearUsuario")
def crearUsuario():
    req = Usuarios.create(**request.get_json())
    return {"status": "ok", "valores": req.to_dict()}


@app.put("/api/actualizarUsuario/<int:usuario_id>")
def actualizarUsuario(usuario_id):
    req = Usuarios.find_or_fail(usuario_id)
    req.update(**request.get_json())
    return {"status": "ok", "id": usuario_id, "values": "se actualizó correctamente"}


@app.delete("/api/eliminarUsuario/<int:usuario_id>")
def eliminarUsuario(usuario_id):
    req = Usuarios.find_or_fail(usuario_id)
    req.delete()
    return {"status": "ok", "id": usuario_id, "values": "se eliminó correctamente"}


if __name__ == "__main__":
    app.run(debug=True)
