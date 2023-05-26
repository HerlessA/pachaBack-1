from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, TextAreaField,DateField,validators
from wtforms.validators import DataRequired, Length


class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    descripcion = StringField('Descripcion')
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    dni = StringField('Dni', validators=[DataRequired(), Length(max=12)])
    celular = StringField('Celular')
    direccion = StringField('Dirección')
    submit = SubmitField('Enviar')


class FacturaForm(FlaskForm):
    fecha = DateField('Fecha', validators=[DataRequired()])
    cliente_id = IntegerField('Cliente', validators=[DataRequired()])
    user_id = IntegerField('Trabajador', validators=[DataRequired()])
    submit = SubmitField('Enviar')
