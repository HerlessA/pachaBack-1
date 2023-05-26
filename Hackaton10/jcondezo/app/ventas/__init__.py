from flask import Blueprint

producto_bp = Blueprint('producto', __name__, template_folder='templates')
cliente_bp = Blueprint('cliente', __name__, template_folder='templates')
factura_bp = Blueprint('factura', __name__, template_folder='templates')

from . import routes