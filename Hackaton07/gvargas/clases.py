class Salones:
    def __init__(self, Nombre, Año, Con):
        self.Nombre = Nombre
        self.Año = Año
        self.Con = Con

class Persona:
    def __init__(self,Id, Nombre, Edad, Correo, Salon, Con ):
        self.Id = Id
        self.Nombre = Nombre
        self.Edad = Edad
        self.Correo = Correo
        self.Salon = Salon
        self.Con = Con

class Alumnos(Persona):
    def __init__(self,IdAlumno, Nombre, Edad, Correo, Salon, Con, Notas ):
        super().__init__(IdAlumno, Nombre, Edad, Correo, Salon, Con)
        self.Notas = Notas

class Profesores(Persona):
    def __init__(self,IdProfesor, Nombre, Edad, Correo, Salon, Con):
        super().__init__(IdProfesor, Nombre, Edad, Correo, Salon, Con)

class Cursos:
    def __init__(self, Nombre, Profesor, Con):
        self.Nombre = Nombre
        self.Profesor = Profesor
        self.Con = Con
