from flask import Flask, jsonify, request

app = Flask(__name__)

# Creación de diccionarios para almacenar la información de alumnos, salones, cursos y profesores
alumnos = {}
salones = {}
cursos = {}
profesores = {}

# Rutas de API para manipulación de datos de alumnos
@app.route('/alumnos', methods=['POST'])
def agregar_alumno():
    alumno = request.get_json()
    identificador = alumno['identificador']
    alumnos[identificador] = alumno
    return jsonify(alumno)

@app.route('/alumnos/<identificador>', methods=['GET'])
def obtener_alumno(identificador):
    return jsonify(alumnos[identificador])

@app.route('/alumnos/<identificador>', methods=['PUT'])
def actualizar_alumno(identificador):
    alumno = request.get_json()
    alumnos[identificador] = alumno
    return jsonify(alumno)

@app.route('/alumnos/<identificador>', methods=['DELETE'])
def eliminar_alumno(identificador):
    del alumnos[identificador]
    return '', 204

# Rutas de API para manipulación de datos de salones
@app.route('/salones', methods=['POST'])
def agregar_salon():
    salon = request.get_json()
    nombre = salon['nombre']
    salones[nombre] = salon
    return jsonify(salon)

@app.route('/salones/<nombre>', methods=['GET'])
def obtener_salon(nombre):
    return jsonify(salones[nombre])

@app.route('/salones/<nombre>', methods=['PUT'])
def actualizar_salon(nombre):
    salon = request.get_json()
    salones[nombre] = salon
    return jsonify(salon)

@app.route('/salones/<nombre>', methods=['DELETE'])
def eliminar_salon(nombre):
    del salones[nombre]
    return '', 204

# Rutas de API para manipulación de datos de cursos
@app.route('/cursos', methods=['POST'])
def agregar_curso():
    curso = request.get_json()
    nombre = curso['nombre']
    cursos[nombre] = curso
    return jsonify(curso)

@app.route('/cursos/<nombre>', methods=['GET'])
def obtener_curso(nombre):
    return jsonify(cursos[nombre])

@app.route('/cursos/<nombre>', methods=['PUT'])
def actualizar_curso(nombre):
    curso = request.get_json()
    cursos[nombre] = curso
    return jsonify(curso)

@app.route('/cursos/<nombre>', methods=['DELETE'])
def eliminar_curso(nombre):
    del cursos[nombre]
    return '', 204

# Rutas de API para manipulación de datos de profesores
@app.route('/profesores', methods=['POST'])
def agregar_profesor():
    profesor = request.get_json()
    identificador = profesor['identificador']
    profesores[identificador] = profesor
    return jsonify(profesor)

@app.route('/profesores/<identificador>', methods=['GET'])
def obtener_profesor(identificador):
    return jsonify(profesores[identificador])

@app.route('/profesores/<identificador>', methods=['PUT'])
def actualizar_profesor(identificador):
    profesor = request.get_json()
    profesores[identificador] = profesor
    return jsonify(profesor)

@app.route('/profesores/<identificador>', methods=['DELETE'])
def eliminar_profesor(identificador):
    del profesores[identificador]
    return '', 204

if __name__ == '__main
