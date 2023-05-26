from flask import render_template, redirect, url_for
from flask_login import login_required

from . import product_bp
from .forms import ProductForm
from app.models import Product


@product_bp.route("/product/", methods=["GET", "POST"])
@login_required
def product_form():
    form = ProductForm()

    if form.validate_on_submit():
        name = form.name.data
        stock = form.stock.data
        price = form.price.data

        product = Product(name=name, stock=stock, price=price)
        product.save()

        return redirect(url_for("public.index"))
    return render_template("product/product_form.html", form=form)
