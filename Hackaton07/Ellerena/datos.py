def conectar_db():
    conexion = psycopg2.connect(database="a0973286", user="postgres", password="gabo", host="localhost", port="5432")
    cursor = conexion.cursor()
    return conexion, cursor

class Persona:
    def __init__(self, nombre, identificador, edad, correo):
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo

class Alumno(Persona):
    def insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO alumnos (nombre, identificador, edad, correo) VALUES (%s, %s, %s, %s);"
        datos = (self.nombre, self.identificador, self.edad, self.correo)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()

    def actualizar(self, conexion):
        cursor = conexion.cursor()
        query = "UPDATE alumnos SET nombre=%s, edad=%s, correo=%s WHERE identificador=%s;"
        datos = (self.nombre, self.edad, self.correo, self.identificador)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()

    def eliminar(self, conexion):
        cursor = conexion.cursor()
        query = "DELETE FROM alumnos WHERE identificador=%s;"
        datos = (self.identificador,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()

    @staticmethod
    def seleccionar(identificador, conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM alumnos WHERE identificador=%s;"
        datos = (identificador,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        if resultado is None:
            return None
        else:
            nombre, identificador, edad, correo = resultado
            return Alumno(nombre, identificador, edad, correo)

    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO alumnos (nombre, identificador, edad, correo) VALUES (%s, %s, %s, %s);"
        datos = (self.nombre, self.identificador, self.edad, self.correo)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE alumnos SET nombre=%s, edad=%s, correo=%s WHERE identificador=%s;"
        datos = (self.nombre, self.edad, self.correo, self.identificador)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM alumnos WHERE identificador=%s;"
        datos = (self.identificador,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(identificador):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM alumnos WHERE identificador=%s;"
        datos = (identificador,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, identificador, edad, correo = resultado
            return Alumno(nombre, identificador, edad, correo)

class Salon:
    def __init__(self, nombre, anio_escolar):
        self.nombre = nombre
        self.anio_escolar = anio_escolar

    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO salones (nombre, anio_escolar) VALUES (%s, %s);"
        datos = (self.nombre, self.anio_escolar)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE salones SET anio_escolar=%s WHERE nombre=%s;"
        datos = (self.anio_escolar, self.nombre)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM salones WHERE nombre=%s;"
        datos = (self.nombre,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(nombre):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM salones WHERE nombre=%s;"
        datos = (nombre,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, anio_escolar = resultado
            return Salon(nombre, anio_escolar)

    def __init__(self, nombre, anio_escolar):
        self.nombre = nombre
        self.anio_escolar = anio_escolar

    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO salones (nombre, anio_escolar) VALUES (%s, %s);"
        datos = (self.nombre, self.anio_escolar)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE salones SET anio_escolar=%s WHERE nombre=%s;"
        datos = (self.anio_escolar, self.nombre)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM salones WHERE nombre=%s;"
        datos = (self.nombre,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(nombre):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM salones WHERE nombre=%s;"
        datos = (nombre,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, anio_escolar = resultado
            return Salon(nombre, anio_escolar)

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO cursos (nombre, profesor) VALUES (%s, %s);"
        datos = (self.nombre, self.profesor.identificador)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE cursos SET profesor=%s WHERE nombre=%s;"
        datos = (self.profesor.identificador, self.nombre)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM cursos WHERE nombre=%s;"
        datos = (self.nombre,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(nombre):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM cursos WHERE nombre=%s;"
        datos = (nombre,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, profesor_id = resultado
            profesor = Profesor.seleccionar(profesor_id)
            return Curso(nombre, profesor)

    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO cursos (nombre, profesor) VALUES (%s, %s);"
        datos = (self.nombre, self.profesor)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE cursos SET profesor=%s WHERE nombre=%s;"
        datos = (self.profesor, self.nombre)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM cursos WHERE nombre=%s;"
        datos = (self.nombre,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(nombre):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM cursos WHERE nombre=%s;"
        datos = (nombre,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, profesor = resultado
            return Curso(nombre, profesor)

class Profesor(Persona):
    def insertar(self):
        conexion, cursor = conectar_db()
        query = "INSERT INTO profesores (nombre, identificador, edad, correo) VALUES (%s, %s, %s, %s);"
        datos = (self.nombre, self.identificador, self.edad, self.correo)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self):
        conexion, cursor = conectar_db()
        query = "UPDATE profesores SET nombre=%s, edad=%s, correo=%s WHERE identificador=%s;"
        datos = (self.nombre, self.edad, self.correo, self.identificador)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion, cursor = conectar_db()
        query = "DELETE FROM profesores WHERE identificador=%s;"
        datos = (self.identificador,)
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def seleccionar(identificador):
        conexion, cursor = conectar_db()
        query = "SELECT * FROM profesores WHERE identificador=%s;"
        datos = (identificador,)
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado is None:
            return None
        else:
            nombre, identificador, edad, correo = resultado
            return Profesor(nombre, identificador, edad, correo)

    def insertar_db(self, conexion):
        query = "INSERT INTO profesores (nombre, identificador, edad, correo) VALUES (%s, %s, %s, %s);"
        datos = (self.nombre, self.identificador, self.edad, self.correo)
        cursor = conexion.cursor()
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()

    def actualizar_db(self, conexion):
        query = "UPDATE profesores SET nombre=%s, edad=%s, correo=%s WHERE identificador=%s;"
        datos = (self.nombre, self.edad, self.correo, self.identificador)
        cursor = conexion.cursor()
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()

    def eliminar_db(self, conexion):
        query = "DELETE FROM profesores WHERE identificador=%s;"
        datos = (self.identificador,)
        cursor = conexion.cursor()
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()

    @staticmethod
    def seleccionar_db(conexion, identificador):
        query = "SELECT * FROM profesores WHERE identificador=%s;"
        datos = (identificador,)
        cursor = conexion.cursor()
        cursor.execute(query, datos)
        resultado = cursor.fetchone()
        cursor.close()
        if resultado is None:
            return None
        else:
            nombre, identificador, edad, correo = resultado
            return Profesor(nombre, identificador, edad, correo)
