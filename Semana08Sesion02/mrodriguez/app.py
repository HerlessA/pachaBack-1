import os
from flask import Flask, request  # request: para peticiones http
from flask_orator import Orator, jsonify  # ORM, convertidor resp de db a json


# Trayendo relaciones del ORM
# belongs_to: uno a muchos
# has_many: muchos a uno
# belongs_to_many: muchos a muchos
from orator.orm import belongs_to, has_many, belongs_to_many

from flask_swagger_ui import get_swaggerui_blueprint
import json


# from modelos import User

# Configuration
DEBUG = True  # para ver los errores

# conector para config Base de datos
ORATOR_DATABASES = {
    "default": "twittor",
    "twittor": {
        "driver": "postgres",
        "host": "localhost",
        "user": "postgres",
        "password": "pSecret6#",
        "database": "twittor",
    },
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
# convirtiendo a json
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
# config swagger
SWAGGER_URL = "/swagger"
API_URL = "http://127.0.0.1:5000/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Sample API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/swagger.json")
def swagger():
    with open("swagger.json", "r") as f:
        return jsonify(json.load(f))


# Initializing Orator
db = Orator(app)


# Creando modelo
class User(db.Model):
    # fillable: indica que solo se muesten los datos de campos señalados de la tabla
    __fillable__ = ["name", "email"]
    __hiden__ = ["pivot"]  # oculta el pivot (foreing-key)

    # 1. Indicando que user tiene muchos messages
    @has_many
    def messages(self):
        return Message

    # 2. Indicando muchos users, tienen muchos followers
    @belongs_to_many("followers", "followed_id", "follower_id", with_timestamps=True)
    def followers(self):
        return User

    @belongs_to_many("followers", "follower_id", "followed_id", with_timestamps=True)
    def followed(self):
        return User

    def is_following(self, user):
        return self.followed().where("followed_id", user.id).exists()

    def is_followed_by(self, user):
        return self.followers().where("follower_id", user.id).exists()

    def follow(self, user):
        if not self.is_following(user):
            self.followed().attach(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed().detach(user)


class Message(db.Model):
    # fillable: indica que solo se muesten los datos de campos señalados de la tabla
    __fillable__ = ["content"]

    # 1. Indicando que un message pertenece a un user
    @belongs_to
    def user(self):
        return User


# Creando Rutas USER
# POST
@app.route("/users", methods=["POST"])
def create_user():
    user = User.create(**request.get_json())
    return jsonify(user)


# GET
# traer un usuario
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # user = User.find(user_id)
    # para que evitar traer null, al pasar un id que no existe y responda con un status http:
    user = User.find_or_fail(user_id)
    return jsonify(user)


# traer  todos los usuarios
@app.route("/users", methods=["GET"])
def get_all_user():
    user = User.all()
    return jsonify(user)


# PATCH
# Actualizar campo(s) user
@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())
    return jsonify(user)


# Creando Rutas MESSAGE
# GET
# trayendo messages de un usuario
@app.route("/users/<int:user_id>/messages", methods=["GET"])
def get_user_messages(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user.messages)


# trayendo messages por su id
@app.route("/messages/<int:message_id>", methods=["GET"])
def get_message(message_id):
    message = Message.find_or_fail(message_id)
    return jsonify(message)


# POST
# creando message de un usuario
@app.route("/users/<int:user_id>/messages", methods=["POST"])
def create_messages(user_id):
    user = User.find_or_fail(user_id)
    message = user.messages().create(**request.get_json())
    return jsonify(message)


# PATCH
# actualizando message por su id
@app.route("/messages/<int:message_id>", methods=["PATCH"])
def update_message(message_id):
    message = Message.find_or_fail(message_id)
    message.update(**request.get_json())
    return jsonify(message)


# DELETE
# eliminando message por su id
@app.route("/messages/<int:message_id>", methods=["DELETE"])
def delete_message(message_id):
    message = Message.find_or_fail(message_id)
    message.delete()
    # configurando una respuesta, si es 204 (exitoso)
    return app.response_class("No Content", 204)


# Creando Rutas FOLLOWERS
# GET
# trayendo users a quienes sigue un user
@app.route("/users/<int:user_id>/following", methods=["GET"])
def get_user_followed(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user.followed)


# trayendo seguidores de un user
@app.route("/users/<int:user_id>/followers", methods=["GET"])
def get_user_followers(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user.followers)


# seguir a un user
@app.route("/users/<int:user_id>/following/<int:followed_id>", methods=["PUT"])
def follow_user(user_id, followed_id):
    user = User.find_or_fail(user_id)
    followed = User.find_or_fail(followed_id)
    user.follow(followed)
    return app.response_class("No Content", 204)


# dejar de seguir a un user
@app.route("/users/<int:user_id>/following/<int:followed_id>", methods=["DELETE"])
def unfollow_user(user_id, followed_id):
    user = User.find_or_fail(user_id)
    followed = User.find_or_fail(followed_id)
    user.unfollow(followed)
    return app.response_class("No Content", 204)


# Constructor de un file, es una buena práctica usarlo
# siempre va al final del file
if __name__ == "__main__":
    app.run()
