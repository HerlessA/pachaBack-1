from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length


# creando clases que se hereda de FlaskForm


# REGISTRO
class SignupForm(FlaskForm):
    # Creando campos/elems para html: ejm: SubmitField
    # y Validando Ejm: max caracteres, requerido, tupo email (regex), etc
    name = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Registrar")


# POST - Blog
class PostForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired(), Length(max=128)])
    title_slug = StringField("Título slug", validators=[Length(max=128)])
    content = TextAreaField("Contenido")
    submit = SubmitField("Enviar")


# LOGIN
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Login")
