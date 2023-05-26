from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = "model_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    rol = db.Column(db.String(128), nullable=False)

    # Datos necesarios:
    def __init__(self, name, email, rol):
        self.name = name
        self.email = email
        self.rol = rol

    # Representación
    def __repr__(self):
        return f"<User {self.email}>"

    # Encriptando password:
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Comparando password:
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # add user
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    # Métodos:
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
