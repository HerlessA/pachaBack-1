from flask_login import UserMixin

# BUENA PRÁCTICA
# werkzeug.security: para crear hash y no grabar el password en la bd (se encripta, no se visualiza)
from werkzeug.security import generate_password_hash, check_password_hash


# Clase user que hereda de UserMixin
class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # validando password
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.email)


# Listado de usuarios
users = []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None
