from db import db


class Libros:
    def __init__(self, titulo, fecPublicacion, isbn, autor):
        # self.id = id
        self.titulo = titulo
        self.fecPublicacion = fecPublicacion
        self.isbn = isbn
        self.autor = autor

    def crearLibro(self):
        conn = db()
        query = f"""insert into Libros(titulo, fecPublicacion, isbn, autor) 
        VALUES ('{self.titulo}', '{self.fecPublicacion}', '{self.isbn}', {self.autor})"""
        return conn.ejecutarBDD(query)

    def traerLibros():
        conn = db()
        query = f"SELECT * FROM Libros"
        return conn.consultarBDD(query)

    def traerLibro():
        conn = db()
        query = f"SELECT * FROM Libros WHERE id = 1"
        return conn.consultarBDD(query)
