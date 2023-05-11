from flask import Flask, render_template, request, redirect, url_for, flash
from config import OratorConfig
from orator import DatabaseManager
from models import Alumno, Profesor, Salon, Curso, Bimestre, Nota, authenticate_user
import psycopg2

app = Flask(__name__)
app.config.from_object(OratorConfig)
db = DatabaseManager(app.config['ORATOR_DATABASES'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("Request method:", request.method)
        email = request.form['email']
        password = request.form['password']
        user = authenticate_user(email, password)
        print(user)  # Depuración: Verificar valor devuelto por authenticate_user

        if user:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Correo electrónico o contraseña incorrectos', 'danger')

    return render_template('login.html')


@app.route('/register_alumno', methods=['GET', 'POST'])
def register_alumno():
    if request.method == 'POST':
        print("Request method:", request.method)
        # Recopilar datos del formulario
        nombre_form = request.form['nombre']
        apellido_form = request.form['apellido']
        correo_form = request.form['correo']
        password_form = request.form['password']
        salon_id_form = request.form['salon_id']

        # Crear y guardar el nuevo alumno
        alumno = Alumno(nombre=nombre_form, apellido=apellido_form, correo=correo_form, password=password_form, salon_id=salon_id_form)
        alumno.save()
        


    salones = Salon.all()
    return render_template('register_alumno.html', salones=salones)



@app.route('/register_profesor', methods=['GET', 'POST'])
def register_profesor():
    if request.method == 'POST':
        # Recopilar datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        password = request.form['password']
        salon_id = request.form['salon_id']

        # Crear y guardar el nuevo profesor
        profesor = Profesor(nombre=nombre, apellido=apellido, correo=correo, password=password, salon_id=salon_id)
        profesor.save()

        flash('Profesor registrado con éxito', 'success')
        return redirect(url_for('index'))

    salones = Salon.all()
    return render_template('register_profesor.html', salones=salones)


@app.route('/bimestres', methods=['GET', 'POST'])
def create_bimestre():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        anio_escolar = request.form['anio_escolar']

        bimestre = Bimestre(nombre=nombre, descripcion=descripcion, anio_escolar=anio_escolar)
        bimestre.save()

        flash('Bimestre creado con éxito', 'success')
        return redirect(url_for('index'))

    return render_template('bimestres.html')

@app.route('/cursos', methods=['GET', 'POST'])
def create_curso():
    print("Request method:", request.method)
    if request.method == 'POST':
        nombre = request.form['nombre']
        salon_id = request.form['salon_id']

        curso = Curso(nombre=nombre, salon_id=salon_id)
        curso.save()

        flash('Curso creado con éxito', 'success')
        return redirect(url_for('index'))

    salones = Salon.all()
    return render_template('cursos.html', salones=salones)



if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    app.run(debug=True)
