class Alumno:
    def __init__(
        self,
        IdAlumno,
        IdentificadorAlumno,
        Nombre,
        Edad,
        Correo,
    ):
        self.IdAlumno = IdAlumno
        self.IdentificadorAlumno = IdentificadorAlumno
        self.Nombre = Nombre
        self.Edad = Edad
        self.Correo = Correo


    def __str__(self):
        return f"idAlumno: {self.IdAlumno}, IdentificadorAlumno: {self.IdentificadorAlumno}, Nombre: {self.Nombre}, Edad: {self.Edad}, Correo: {self.Correo}"