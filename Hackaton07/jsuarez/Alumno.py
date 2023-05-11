class Alumno:
    def __init__(
        self,
        identificador,
        nombre,
        edad,
        correo,
    ):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.correo = correo


    def __str__(self):
        return f"idAlumno: {self.IdAlumno}, Identificador: {self.Identificador}, Nombre: {self.Nombre}, Edad: {self.Edad}, Correo: {self.Correo}"