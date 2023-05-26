from flask import render_template, redirect, url_for
from . import producto_bp, cliente_bp, factura_bp
from flask_login import login_required, current_user
from .forms import ProductoForm, ClienteForm, FacturaForm
from app.models import Producto, Cliente, Factura, DetalleFactura

@producto_bp.route("/productos/", methods=['GET', 'POST'])
@login_required
def productos_form():
    form = ProductoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        cantidad = form.cantidad.data
        marca = form.marca.data
        precio = form.precio.data
        prod = Producto(nombre = nombre, descripcion = descripcion, cantidad = cantidad, marca = marca, precio = precio)
        prod.save()

        productos = Producto.get_all()

        return render_template("productos/view_producto.html", productos=productos)
    return render_template("productos/producto_form.html", form=form)

@cliente_bp.route("/clientes/", methods=['GET', 'POST'])
@login_required
def clientes_form():
    form = ClienteForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        dni = form.dni.data
        celular = form.celular.data
        direccion = form.direccion.data
        cliente = Cliente(nombre = nombre, dni = dni, celular = celular, direccion = direccion)
        cliente.save()

        clientes = Cliente.get_all()

        return render_template("clientes/view_cliente.html", clientes=clientes)
    return render_template("clientes/cliente_form.html", form=form)


@factura_bp.route("/facturas/", methods=['GET', 'POST'])
@login_required
def facturas_form():
    form = FacturaForm()
    if form.validate_on_submit():
        fecha = form.fecha.data
        cliente_id = form.cliente_id.data
        factura = Factura(fecha = fecha, cliente_id = cliente_id, user_id = current_user.id)
        factura.save()

        facturas = Factura.get_all()

        return render_template("facturas/view_factura.html", facturas=facturas)
    return render_template("facturas/factura_form.html", form=form)