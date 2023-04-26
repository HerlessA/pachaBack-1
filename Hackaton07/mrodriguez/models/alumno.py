from models.persona import Persona


class Alumno(Persona):
    def __init__(self, id, nombre, dni, edad, correo, notas):
        super().__init__(id, nombre, dni, edad, correo)
        self.notas = notas
