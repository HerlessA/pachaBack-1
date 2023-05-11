from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many
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
        'password': 'pacha23',
        'database': 'twittor'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/swagger.json'
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

# Initializing Orator
db = Orator(app)



#Modelos
class User(db.Model):
    __fillable__ = ['name', 'email']
    __hidden__ = ['pivot']
    @has_many
    def messages(self):
        return Message

    @belongs_to_many(
        'followers',
        'followed_id', 'follower_id',
        with_timestamps=True
    )
    def followers(self):
        return User

    @belongs_to_many(
        'followers',
        'follower_id', 'followed_id',
        with_timestamps=True
    )
    def followed(self):
        return User
    
    def is_following(self, user):
        return self.followed().where('followed_id', user.id).exists()

    def is_followed_by(self, user):
        return self.followers().where('follower_id', user.id).exists()

    def follow(self, user):
        if not self.is_following(user):
            self.followed().attach(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed().detach(user)


class Message(db.Model):
    __fillable__ = ['content']
    @belongs_to
    def user(self):
        return User


#Rutas
@app.route('/users', methods=['POST'])
def create_user():
    user = User.create(**request.get_json())
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user)

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.all()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())
    return jsonify(user)

@app.route('/users/<int:user_id>/messages', methods=['GET'])
def get_user_messages(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user.messages)

@app.route('/users/<int:user_id>/messages', methods=['POST'])
def create_message(user_id):
    user = User.find_or_fail(user_id)
    message = user.messages().create(**request.get_json())
    return jsonify(message)

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

@app.route('/users/<int:user_id>/following', methods=['GET'])
def get_user_followed(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user.followed)

@app.route('/users/<int:user_id>/followers', methods=['GET'])
def get_user_followers(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user.followers)

@app.route('/users/<int:user_id>/following/<int:followed_id>', methods=['PUT'])
def follow_user(user_id, followed_id):
    user = User.find_or_fail(user_id)
    followed = User.find_or_fail(followed_id)
    user.follow(followed)
    return app.response_class('No Content', 204)

@app.route('/users/<int:user_id>/following/<int:followed_id>', methods=['DELETE'])
def unfollow_user(user_id, followed_id):
    user = User.find_or_fail(user_id)
    followed = User.find_or_fail(followed_id)
    user.unfollow(followed)
    return app.response_class('No Content', 204)

if __name__ == '__main__':
    app.run()