class Profesor:
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
        return f"IdentificadorProfesor: {self.identificador}, Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"