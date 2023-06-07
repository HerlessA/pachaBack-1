from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('minimarket_user.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(256), nullable=False)
    name_slug = db.Column(db.String(256), unique=True, nullable=False)
    stock = db.Column(db.String(256), nullable=False)
    price = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}  >"  # {self.name_slug} {self.stock} {self.price}

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.name_slug:
            self.name_slug = slugify(self.name)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.name_slug = f"{self.name_slug}-{count}"

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def public_url(self):
        return url_for("public.show_product", slug=self.name_slug)

    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    @staticmethod
    def get_by_slug(slug):
        return Product.query.filter_by(name_slug=slug).first()

    @staticmethod
    def get_all():
        return Product.query.all()
