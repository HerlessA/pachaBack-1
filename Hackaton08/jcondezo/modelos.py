from app import db

class User(db.Model):
    __fillable__ = ['name', 'email']