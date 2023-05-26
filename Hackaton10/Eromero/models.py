from orator import Model, DatabaseManager
from orator.orm import belongs_to
from flask_login import UserMixin
from config import db

Model.set_connection_resolver(db)

class Usuario(UserMixin, Model):
    __table__ = 'usuarios'
    __fillable__ = ['nombre', 'correo', 'password', 'rol']

class Producto(Model):
    __table__ = 'productos'
    __fillable__ = ['nombre', 'categoria', 'stock', 'precio']

class Factura(Model):
    __table__ = 'facturas'
    __fillable__ = ['usuario_id', 'producto_id', 'cantidad', 'total']

    @belongs_to
    def usuario(self):
        return Usuario

    @belongs_to
    def producto(self):
        return Producto
