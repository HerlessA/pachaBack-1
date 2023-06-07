from models.persona import Persona


class Alumno(Persona):
    def __init__(self, nombre, dni, edad, correo, id):
        super().__init__(nombre, dni, edad, correo)
        self.id = id
