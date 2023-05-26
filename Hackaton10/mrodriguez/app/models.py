from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


class Product(db.Model):
    __tablename__ = "model_product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    stock = db.Column(db.String(256), nullable=False)
    price = db.Column(db.String(256), nullable=False)

    # Datos necesarios:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    # Representación
    def __repr__(self):
        return f"<Product {self.name} {self.stock} {self.price} >"

    # add product
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

    # Métodos:
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    # @staticmethod
    # def query_all(id):
    #     return Product.query.all(id)
