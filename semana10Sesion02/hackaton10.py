from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de ejemplo (puedes reemplazarlos con una base de datos)
productos = [
    {'id': 1, 'nombre': 'Producto 1', 'stock': 10, 'precio': 10.99},
    {'id': 2, 'nombre': 'Producto 2', 'stock': 5, 'precio': 5.99},
    {'id': 3, 'nombre': 'Producto 3', 'stock': 2, 'precio': 2.99}
]

# Rutas de la aplicación

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para el rol de Almacén

# Mostrar la lista de productos
@app.route('/almacen/productos')
def almacen_productos():
    return render_template('almacen_productos.html', productos=productos)

# Actualizar la información de un producto
@app.route('/almacen/productos/<int:producto_id>/actualizar', methods=['GET', 'POST'])
def almacen_actualizar_producto(producto_id):
    # Obtener el producto de la lista según su ID
    producto = next((p for p in productos if p['id'] == producto_id), None)

    if request.method == 'POST':
        # Actualizar la información del producto según los datos enviados en el formulario
        producto['stock'] = request.form['stock']
        producto['precio'] = request.form['precio']
        return redirect(url_for('almacen_productos'))

    return render_template('almacen_actualizar_producto.html', producto=producto)

# Rutas para el rol de Cajero

# Página de ventas
@app.route('/cajero/ventas', methods=['GET', 'POST'])
def cajero_ventas():
    if request.method == 'POST':
        # Procesar la venta y generar la factura o boleta
        # Aquí puedes agregar la lógica para calcular el total, actualizar el stock, etc.
        return redirect(url_for('cajero_ventas'))

    return render_template('cajero_ventas.html', productos=productos)

# Rutas para el rol de Administrador

# Ver el reporte de ventas del día o mes
@app.route('/admin/reportes')
def admin_reportes():
    # Lógica para generar los reportes de ventas
    return render_template('admin_reportes.html')


if __name__ == '__main__':
    app.run(debug=True)
