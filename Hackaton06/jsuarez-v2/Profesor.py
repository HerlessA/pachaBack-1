class Profesor:
    def __init__(
        self,
        IdProfesor,
        IdentificadorProfesor,
        Nombre,
        Edad,
        Correo,
    ):
        self.IdProfesor = IdProfesor
        self.IdentificadorProfesor = IdentificadorProfesor
        self.Nombre = Nombre
        self.Edad = Edad
        self.Correo = Correo


    def __str__(self):
        return f"IdProfesor: {self.IdProfesor}, IdentificadorProfesor: {self.IdentificadorProfesor}, Nombre: {self.Nombre}, Edad: {self.Edad}, Correo: {self.Correo}"