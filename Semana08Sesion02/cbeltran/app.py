import os
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many

# Configuracion
DEBUG = True
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'root',
        'database': 'twittor'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Inicializando Orator
db = Orator(app)

if __name__ == '__main__':
    app.run()


#------------------------------------------------------MODELOS-----------------------------------------------------
#Modelo de Usuario
class User(db.Model):
    __fillable__ = ['name', 'email']

    @has_many
    def messages(self):
        return Message
#Modelo de Mensaje
class Message(db.Model):
    __fillable__ = ['content']

    @belongs_to
    def user(self):
        return User

#------------------------------------------------------RUTAS-----------------------------------------------------

#Ruta para CREAR un usuario
@app.route('/users', methods=['POST'])
def create_user():
    user = User.create(**request.get_json())

    return jsonify(user)

#Ruta para obtener información de un solo usuario(LISTAR USUARIO)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user)

#Ruta para obtener información de todos los usuarios(LISTAR USUARIOS)
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.all()

    return jsonify(users)

#Ruta para ACTUALIZAR un usuario
@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())

    return jsonify(user)

#Ruta para obtener la información de un solo mensaje de un solo usuario
@app.route('/users/<int:user_id>/messages', methods=['GET'])
def get_user_messages(user_id):
    user = User.find_or_fail(user_id)

    return jsonify(user.messages)

#Ruta para crear nuevos mensajes
@app.route('/users/<int:user_id>/messages', methods=['POST'])
def create_message(user_id):
    user = User.find_or_fail(user_id)
    message = user.messages().create(**request.get_json())

    return jsonify(message)

#Creamos rutas para OBTENER, ACTUALIZAR y BORRAR un mensaje.
@app.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.find_or_fail(message_id)

    return jsonify(message)

@app.route('/messages/<int:message_id>', methods=['PATCH'])
def update_message(message_id):
    message = Message.find_or_fail(message_id)
    message.update(**request.get_json())

    return jsonify(message)

@app.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.find_or_fail(message_id)
    message.delete()

    return app.response_class('No Content', 204)