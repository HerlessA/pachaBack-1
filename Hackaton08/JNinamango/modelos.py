from app import db

#create tables:
#crear estructura de tabla: python db.py make:migration create_users_table --table users --create
#confirmar creacion:  python db.py migrate
#confirmar migracion u operacion: python db.py migrate:status

class User(db.Model):
    __fillable__ = ['name', 'email']
