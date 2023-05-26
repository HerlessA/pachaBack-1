from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from models import Usuario, Producto, Factura
from config import OratorConfig

app = Flask(__name__)
app.config.from_object(OratorConfig)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.find(user_id)

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        user = Usuario.where('correo', correo).where('password', password).first()
        if user:
            login_user(user)
            if user.rol == 'Administrador':
                return redirect(url_for('admin'))
            elif user.rol == 'Cajero':
                return redirect(url_for('ventas'))
            elif user.rol == 'Almacen':
                return redirect(url_for('almacen'))
            else:
                return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Correo y/o contraseña incorrectos.")
    else:
        return render_template('login.html')

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/admin/crear_usuario', methods=['GET', 'POST'])
@login_required
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        password = request.form.get('password')
        rol = request.form.get('rol')
        Usuario.create(nombre=nombre, correo=correo, password=password, rol=rol)
        return redirect(url_for('admin'))
    else:
        return render_template('crear_usuario.html')


@app.route('/admin/crear_producto', methods=['GET', 'POST'])
@login_required
def crear_producto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        categoria = request.form.get('categoria')
        stock = request.form.get('stock')
        precio = request.form.get('precio')
        Producto.create(nombre=nombre, categoria=categoria, stock=stock, precio=precio)
        return redirect(url_for('admin'))
    else:
        return render_template('crear_producto.html')

@app.route('/admin/ver_usuarios')
@login_required
def ver_usuarios():
    usuarios = Usuario.all()
    return render_template('ver_usuarios.html', usuarios=usuarios)


@app.route('/admin/ver_productos')
@login_required
def ver_productos():
    productos = Producto.all()
    return render_template('ver_productos.html', productos=productos)


@app.route('/ventas')
@login_required
def ventas():
    return render_template('ventas.html')

@app.route('/ventas/seleccionar_producto', methods=['GET', 'POST'])
@login_required
def seleccionar_producto():
    if request.method == 'POST':
        producto_id = request.form.get('producto_id')
        producto = Producto.find(producto_id)
        if producto.stock > 0:
            return redirect(url_for('procesar_venta', producto_id=producto_id))
        else:
            return render_template('seleccionar_producto.html', error="Producto sin stock.")
    else:
        productos = Producto.all()
        return render_template('seleccionar_producto.html', productos=productos)

@app.route('/ventas/procesar_venta/<producto_id>', methods=['GET', 'POST'])
@login_required
def procesar_venta(producto_id):
    if request.method == 'POST':
        cantidad = int(request.form.get('cantidad'))
        producto = Producto.find(producto_id)
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            producto.save()
            total = producto.precio * cantidad
            factura = Factura.create(producto_id=producto_id, cantidad=cantidad, total=total)
            return redirect(url_for('factura', factura_id=factura.id))
        else:
            return render_template('procesar_venta.html', error="Cantidad insuficiente en stock.")
    else:
        producto = Producto.find(producto_id)
        return render_template('procesar_venta.html', producto=producto)

@app.route('/ventas/factura/<factura_id>')
@login_required
def factura(factura_id):
    factura = Factura.find(factura_id)
    return render_template('factura.html', factura=factura)


@app.route('/almacen')
@login_required
def almacen():
    productos = Producto.all()
    return render_template('almacen.html', productos=productos)

@app.route('/almacen/ver_productos')
@login_required
def ver_productos_almacen():
    busqueda = request.args.get('busqueda', '')
    productos = Producto.where('nombre', 'like', '%{}%'.format(busqueda)).get()
    return render_template('ver_productos_almacen.html', productos=productos)


@app.route('/almacen/modificar_producto/<producto_id>', methods=['GET', 'POST'])
@login_required
def modificar_producto(producto_id):
    producto = Producto.find(producto_id)
    if request.method == 'POST':
        producto.nombre = request.form.get('nombre')
        producto.categoria = request.form.get('categoria')
        producto.stock = request.form.get('stock')
        producto.precio = request.form.get('precio')
        producto.save()
        return redirect(url_for('ver_productos_almacen'))
    else:
        return render_template('modificar_producto.html', producto=producto)

@app.route('/almacen/eliminar_producto/<producto_id>', methods=['POST'])
@login_required
def eliminar_producto(producto_id):
    producto = Producto.find(producto_id)
    producto.delete()
    return redirect(url_for('ver_productos_almacen'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
