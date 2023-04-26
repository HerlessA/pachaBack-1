class Curso:
    def __init__(
        self,
        IdCurso,
        Nombre,
        IdentificadorCurso,
    ):
        self.IdCurso = IdCurso
        self.Nombre = Nombre
        self.IdentificadorCurso = IdentificadorCurso


    def __str__(self):
        return f"IdCurso: {self.IdCurso},IdentificadorCurso: {self.IdentificadorCurso}, Nombre: {self.Nombre}"
