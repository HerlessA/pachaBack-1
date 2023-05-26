from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, validators
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        "Nombre de producto", validators=[DataRequired(), Length(max=128)]
    )
    stock = StringField("Stock", validators=[DataRequired(), Length(max=128)])
    price = StringField("Precio", validators=[DataRequired(), Length(max=128)])
    submit = SubmitField("Enviar")
