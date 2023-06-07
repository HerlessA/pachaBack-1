from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    username = StringField(
        "Nombre de usuario", validators=[DataRequired(), Length(max=64)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    rol = StringField(
        "Rol (Administrador, Cajero o Almacén)", validators=[DataRequired()]
    )
    submit = SubmitField("Registrar")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Login")
