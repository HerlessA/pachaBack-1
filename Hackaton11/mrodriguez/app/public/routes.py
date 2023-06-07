import logging
from flask import abort, render_template
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from app.models import Product
from . import public_bp

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    products = Product.get_all()
    return render_template("public/index.html", products=products)


@public_bp.route("/p/<string:slug>/", methods=["GET", "POST"])
def show_product(slug):
    product = Product.get_by_slug(slug)
    if not product:
        logger.info(f"El producto {slug} no existe")
        abort(404)
    return render_template("public/product_view.html", product=product)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    product = Product.get_all()
    return render_template("public/index.html", product=product)
