from flask import Flask

# render_template: renderiza html
# request: objeto, contiene la info que envía el user al servidor
from flask import render_template, request, redirect, url_for

from flask_login import (
    LoginManager,
    logout_user,
    current_user,
    login_user,
    login_required,
)
from werkzeug.urls import url_parse

from forms import SignupForm, PostForm, LoginForm
from models import users, get_user, User

# ********************************************************

app = Flask(__name__)
# Por defecto, Flask-WTF genera para todas las instancias de la clase FlaskForm un campo oculto
#  que contiene un token y sirve para proteger nuestra aplicación contra ataques CSRF (robo de info).
# "SECRET_KEY": Llave para asegurar el envío de info entre el form y web que recibe:
app.config[
    "SECRET_KEY"
] = "7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe"

# LOGIN
login_manager = LoginManager(app)
# indicando cuál es la vista para realizar el login
login_manager.login_view = "login"


# Listado de POST (por el momento en lista, luego se envía a la bd)
posts = []


# INDEX
@app.route("/")
def index():
    # return f"Numero de Posts {len(posts)}"
    # page = request.args.get("page", 1)
    # list = request.args.get("list", 20)
    # return render_template("index.html", num_posts=len(posts))
    return render_template("index.html", posts=posts)


# P/SLUG
@app.route("/p/<string:slug>/")
def show_post(slug):
    # return "Mostrando el post {}".format(slug)
    return render_template("post_view.html", slug_title=slug)


# ADMIN/post form
@app.route("/admin/post/", methods=["GET", "POST"], defaults={"post_id": None})
@app.route("/admin/post/<int:post_id>/", methods=["GET", "POST"])
# Flask-login permite proteger el acceso a las vistas solo a los usuarios autenticados:
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data

        post = {"title": title, "title_slug": title_slug, "content": content}
        posts.append(post)

        return redirect(url_for("index"))
    return render_template("admin/post_form.html", form=form)


# REGISTRO
# @app.route("/signup/")
# indicando métodos aceptados del form (para no mostrar error al dar clic en submit)
@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    # validador:
    form = SignupForm()

    # if request.method == "POST":
    # validando envío de form:

    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = SignupForm()
    if form.validate_on_submit():
        # campos requeridos con POST:
        # name = request.form["name"]
        # email = request.form["email"]
        # password = request.form["password"]

        # next = request.args.get("next", None)
        # if next:
        #     return redirect(next)

        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get("next", None)
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(url_for("index"))
    return render_template("signup_form.html", form=form)


# LOGIN
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login_form.html", form=form)


# LOGOUT
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000, debug=True)
