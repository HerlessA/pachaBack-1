from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


class Rol(db.Model):

    __tablename__ = 'model_rol'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Rol {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    @staticmethod
    def get_by_id(slug):
        return Rol.query.filter_by(id=slug).first()

    @staticmethod
    def get_all():
        return Rol.query.all()


class Producto(db.Model):

    __tablename__ = 'model_producto'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    @staticmethod
    def get_by_id(slug):
        return Producto.query.filter_by(id=id).first()

    @staticmethod
    def get_all():
        return Producto.query.all()


class Cliente(db.Model):

    __tablename__ = 'model_cliente'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    dni = db.Column(db.String(12), nullable=False)
    celular = db.Column(db.String(9), nullable=True)
    direccion = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f'<Cliente {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    @staticmethod
    def get_all():
        return Cliente.query.all()


class Factura(db.Model):

    __tablename__ = 'model_factura'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime(), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('model_cliente.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('model_user.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f'<Factura {self.fecha}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    @staticmethod
    def get_all():
        return Factura.query.all()


class DetalleFactura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('model_producto.id', ondelete='CASCADE'), nullable=False)
    factura_id = db.Column(db.Integer, db.ForeignKey('model_factura.id', ondelete='CASCADE'), nullable=False)
    Cantidad = db.Column(db.Integer, nullable=True)
    MontoTotal = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f'<DetalleFactura {self.id}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    @staticmethod
    def get_by_id(slug):
        return DetalleFactura.query.filter_by(id=id).first()