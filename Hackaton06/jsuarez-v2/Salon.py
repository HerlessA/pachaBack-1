class Salon:
    def __init__(
        self,
        IdSalon,
        Nombre,
        AnioEscolar,
        IdentificadorSalon
    ):
        self.IdSalon = IdSalon
        self.IdentificadorSalon = IdentificadorSalon
        self.Nombre = Nombre
        self.AnioEscolar = AnioEscolar


    def __str__(self):
        return f"IdSalon: {self.IdSalon}, IdentificadorSalon: {self.IdentificadorSalon}, Nombre: {self.Nombre}, Anio Escolar: {self.AnioEscolar}"