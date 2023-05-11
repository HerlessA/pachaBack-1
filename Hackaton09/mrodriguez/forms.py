from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    BooleanField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Registrar")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Login")


class AlumnoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=128)])
    dni = StringField("DNI", validators=[Length(max=8)])
    edad = IntegerField("Edad")
    correo = StringField("Correo", validators=[DataRequired(), Email()])
    submit = SubmitField("Enviar")


class ProfesorForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=128)])
    dni = StringField("DNI", validators=[Length(max=8)])
    edad = IntegerField("Edad")
    correo = StringField("Correo", validators=[DataRequired(), Email()])
    submit = SubmitField("Enviar")


class CursoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=128)])
    profesor_id = IntegerField("ID profesor", validators=[DataRequired()])
    submit = SubmitField("Enviar")


class SalonForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=128)])
    periodo = StringField("Periodo", validators=[DataRequired(), Length(max=128)])
    alumno_id = IntegerField("ID alumno", validators=[DataRequired()])
    profesor_id = IntegerField("ID profesor", validators=[DataRequired()])
    submit = SubmitField("Enviar")
