import logging
from flask import render_template, redirect, url_for, abort, request, current_app
from flask_login import login_required, current_user
from app.auth.decorators import admin_required

from app.models import Product
from . import admin_bp
from .forms import ProductForm

logger = logging.getLogger(__name__)


@admin_bp.route(
    "/admin/product/", methods=["GET", "POST"], defaults={"product_id": None}
)

# Crear producto
@admin_bp.route("/admin/product/", methods=["GET", "POST"])
@login_required
@admin_required
def product_form():
    form = ProductForm()
    if form.validate_on_submit():
        name = form.name.data
        name_slug = form.name_slug.data
        stock = form.stock.data
        price = form.price.data
        product = Product(
            name=name, name_slug=name_slug, stock=stock, price=price
        )  # user_id=current_user.id,
        product.save()
        logger.info(f"Guardando nuevo producto {name}")
        return redirect(url_for("public.index"))
    return render_template("admin/product_form.html", form=form)


# Actualizar producto
@admin_bp.route("/admin/product/<int:product_id>/", methods=["GET", "POST"])
@login_required
@admin_required
def update_product_form(product_id):
    product = Product.get_by_id(product_id)
    if product is None:
        logger.info(f"El producto {product_id} no existe.")
        abort(404)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.name_slug = form.name_slug.data
        product.stock = form.stock.data
        product.price = form.price.data
        product.save()
        logger.info(f"Guardando producto {product_id}")
        return redirect(url_for("public.index"))
    return render_template("admin/product_form.html", form=form, product=product)
