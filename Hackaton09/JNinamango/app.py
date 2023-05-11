from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse

from forms import SignupForm, LoginForm, AlumnoForm, ProfesoresForm, CursosForm, SalonesForm
from models import users, get_user, User, Alumnos

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

login_manager = LoginManager(app)
login_manager.login_view = "login"

posts = []
alumnos = []
profesores = []
cursos = []
salones = []

@app.route("/")
def index():
    return render_template("index.html", alumnos=alumnos)


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


@app.route("/admin/alumnos/", methods=['GET', 'POST'])
#@login_required
def alumno_form_function():
    form = AlumnoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        correo = form.correo.data
        identificador = form.identificador.data

        alumno = {'nombre': nombre, 'edad': edad, 'identificador': identificador, 'correo' : correo}
        alumnos.append(alumno)

        return redirect(url_for('index'))
        
    return render_template("admin/alumno_form.html", form=form)

@app.route("/admin/alumnos/borrar/", methods=['GET','POST'])
def alumno_delete_function():

    form = AlumnoForm()
    if form.validate_on_submit():
        for alumno in alumnos:
            if alumno['identificador'] == 0:
                alumnos.remove(alumno)

        return redirect(url_for('index'))

    return render_template("admin/alumno_update.html", form=form)

@app.route("/admin/alumnos/lista", methods=['GET'])
def alumno_get_function():
    return render_template("admin/alumno_list.html", alumnos=alumnos)





@app.route("/admin/profesores/", methods=['GET', 'POST'])
#@login_required
def profesor_form_function():
    form = ProfesoresForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        correo = form.correo.data
        identificador = form.identificador.data

        prof = {'nombre': nombre, 'edad': edad, 'identificador': identificador, 'correo' : correo}
        profesores.append(prof)

        return redirect(url_for('index'))
        
    return render_template("admin/profesor_form.html", form=form)

@app.route("/admin/profesor/borrar/", methods=['GET','POST'])
def profesor_delete_function():

    form = ProfesoresForm()
    if form.validate_on_submit():
        for prof in profesores:
            if prof['identificador'] == 0:
                profesores  .remove(prof)

        return redirect(url_for('index'))

    return render_template("admin/profesor_update.html", form=form)

@app.route("/admin/profesor/lista", methods=['GET'])
def profesor_get_function():
    return render_template("admin/profesor_list.html", profesores=profesores)






@app.route("/admin/cursos/", methods=['GET', 'POST'])
#@login_required
def cursos_form_function():
    form = CursosForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        identificador = form.identificador

        curso = {'nombre': nombre,'identificador': identificador}
        cursos.append(curso)

        return redirect(url_for('index'))
        
    return render_template("admin/cursos_form.html", form=form)

@app.route("/admin/cursos/borrar/", methods=['GET','POST'])
def cursos_delete_function():

    form = CursosForm()
    if form.validate_on_submit():
        for cur in cursos:
            if cur['identificador'] == 0:
                cursos.remove(cur)

        return redirect(url_for('index'))

    return render_template("admin/cursos_update.html", form=form)

@app.route("/admin/cursos/lista", methods=['GET'])
def cursos_get_function():
    return render_template("admin/cursos_list.html", cursos=cursos)









@app.route("/admin/salones/", methods=['GET', 'POST'])
#@login_required
def salones_form_function():
    form = SalonesForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        identificador = form.identificador

        salon = {'nombre': nombre,'identificador': identificador}
        salones.append(salon)

        return redirect(url_for('index'))
        
    return render_template("admin/salones_form.html", form=form)

@app.route("/admin/salones/borrar/", methods=['GET','POST'])
def salones_delete_function():

    form = SalonesForm()
    if form.validate_on_submit():
        for sal in salones:
            if sal['identificador'] == 0:
                salones.remove(sal)

        return redirect(url_for('index'))

    return render_template("admin/salones_update.html", form=form)

@app.route("/admin/salones/lista", methods=['GET'])
def salones_get_function():
    return render_template("admin/salones_list.html", cursos=cursos)



















@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)