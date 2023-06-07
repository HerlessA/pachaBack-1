from model import Libros


class Controller:
    def crearLibro(self, titulo, fecPublicacion, isbn, autor):
        libro = Libros(titulo, fecPublicacion, isbn, autor)
        return libro.crearLibro()

    def traerLibros(self):
        libro = Libros()
        return libro.traerLibros()

    def traerLibro(self, titulo):
        libro = Libros(titulo=titulo)
        return libro.traerLibro()
