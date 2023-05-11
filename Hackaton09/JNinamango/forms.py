from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    identificador = StringField('Identificador', validators=[Length(max=128)])
    edad = IntegerField('Edad')
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')

class ProfesoresForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    identificador = StringField('Identificador', validators=[Length(max=128)])
    edad = IntegerField('Edad')
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')

class SalonesForm(FlaskForm):
    nombre = StringField('Nombre_Salon', validators=[DataRequired(), Length(max=128)])
    identificador = IntegerField('Identificador')
    submit = SubmitField('Enviar')

class CursosForm(FlaskForm):
    nombre = StringField('Nombre_Curso', validators=[DataRequired(), Length(max=128)])
    identificador = IntegerField('Identificador')
    submit = SubmitField('Enviar')
