# Configuración de Flask y rutas de la aplicación aquí
from flask import Flask, jsonify, request
from orator import DatabaseManager
from models import Salon, Alumno, Curso, Nota, Bimestre, Profesor
from config import db

app = Flask(__name__)

# Crear un nuevo alumno
@app.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.json
    alumno = Alumno.create(**data)
    return jsonify(alumno.serialize()), 201

# Leer todos los alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumno.all()
    return jsonify([alumno.serialize() for alumno in alumnos])

# Leer un alumno específico
@app.route('/alumnos/<int:alumno_id>', methods=['GET'])
def get_alumno(alumno_id):
    alumno = Alumno.find(alumno_id)
    if alumno:
        return jsonify(alumno.serialize())
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404

# Actualizar un alumno específico
@app.route('/alumnos/<int:alumno_id>', methods=['PUT'])
def update_alumno(alumno_id):
    data = request.json
    alumno = Alumno.find(alumno_id)
    if alumno:
        alumno.update(**data)
        return jsonify(alumno.serialize())
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404

# Eliminar un alumno específico
@app.route('/alumnos/<int:alumno_id>', methods=['DELETE'])
def delete_alumno(alumno_id):
    alumno = Alumno.find(alumno_id)
    if alumno:
        alumno.delete()
        return jsonify({"message": "Alumno eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Alumno no encontrado"}), 404

# Crear un nuevo salon
@app.route('/salones', methods=['POST'])
def create_salon():
    data = request.json
    salon = Salon.create(**data)
    return jsonify(salon.serialize()), 201

# Leer todos los salones
@app.route('/salones', methods=['GET'])
def get_salones():
    salones = Salon.all()
    return jsonify([salon.serialize() for salon in salones])

# Leer un salon específico
@app.route('/salones/<int:salon_id>', methods=['GET'])
def get_salon(salon_id):
    salon = Salon.find(salon_id)
    if salon:
        return jsonify(salon.serialize())
    else:
        return jsonify({"error": "Salon no encontrado"}), 404

# Actualizar un salon específico
@app.route('/salones/<int:salon_id>', methods=['PUT'])
def update_salon(salon_id):
    data = request.json
    salon = Salon.find(salon_id)
    if salon:
        salon.update(**data)
        return jsonify(salon.serialize())
    else:
        return jsonify({"error": "Salon no encontrado"}), 404

# Eliminar un salon específico
@app.route('/salones/<int:salon_id>', methods=['DELETE'])
def delete_salon(salon_id):
    salon = Salon.find(salon_id)
    if salon:
        salon.delete()
        return jsonify({"message": "Salon eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Salon no encontrado"}), 404

# Crear un nuevo curso
@app.route('/cursos', methods=['POST'])
def create_curso():
    data = request.json
    curso = Curso.create(**data)
    return jsonify(curso.serialize()), 201

# Leer todos los cursos
@app.route('/cursos', methods=['GET'])
def get_cursos():
    cursos = Curso.all()
    return jsonify([curso.serialize() for curso in cursos])

# Leer un curso específico
@app.route('/cursos/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    curso = Curso.find(curso_id)
    if curso:
        return jsonify(curso.serialize())
    else:
        return jsonify({"error": "Curso no encontrado"}), 404

# Actualizar un curso específico
@app.route('/cursos/<int:curso_id>', methods=['PUT'])
def update_curso(curso_id):
    data = request.json
    curso = Curso.find(curso_id)
    if curso:
        curso.update(**data)
        return jsonify(curso.serialize())
    else:
        return jsonify({"error": "Curso no encontrado"}), 404

# Eliminar un curso específico
@app.route('/cursos/<int:curso_id>', methods=['DELETE'])
def delete_curso(curso_id):
    curso = Curso.find(curso_id)
    if curso:
        curso.delete()
        return jsonify({"message": "Curso eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Curso no encontrado"}), 404

@app.route('/bimestres', methods=['POST'])
def create_bimestre():
    data = request.get_json()
    bimestre = Bimestre.create(**data)
    return jsonify(bimestre.serialize()), 201

@app.route('/bimestres', methods=['GET'])
def get_bimestres():
    bimestres = Bimestre.all()
    return jsonify([b.to_dict() for b in bimestres]), 200

@app.route('/bimestres/<int:bimestre_id>', methods=['GET'])
def get_bimestre(bimestre_id):
    bimestre = Bimestre.find(bimestre_id)
    if not bimestre:
        return jsonify({"error": "Bimestre not found"}), 404
    return jsonify(bimestre.serialize()), 200

@app.route('/notas', methods=['POST'])
def create_nota():
    data = request.get_json()
    nota = Nota.create(**data)
    return jsonify(nota.serialize()), 201

@app.route('/notas', methods=['GET'])
def get_notas():
    notas = Nota.all()
    return jsonify([n.to_dict() for n in notas]), 200

@app.route('/notas/<int:nota_id>', methods=['GET'])
def get_nota(nota_id):
    nota = Nota.find(nota_id)
    if not nota:
        return jsonify({"error": "Nota not found"}), 404
    return jsonify(nota.serialize()), 200

@app.route('/profesores', methods=['GET'])
def get_profesores():
    profesores = Profesor.all()
    return jsonify([profesor.serialize() for profesor in profesores])

@app.route('/profesores', methods=['POST'])
def create_profesor():
    data = request.get_json()
    profesor = Profesor.create(**data)
    return jsonify(profesor.serialize()), 201

if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
