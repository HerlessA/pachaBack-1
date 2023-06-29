from db import db
class libros:
    def __init__(self, id, titulo, fecPublicacion, isbn, autor):
        self.id = id
        self.titulo = titulo
        self.fecPublicacion = fecPublicacion
        self.isbn = isbn
        self.autor = autor

    def crearlibro(self, titulo, fecPublicacion, isbn, autor):
        conn = db()
        query = f'''insert into Libros(titulo, fecPublicacion, isbn, autor)
                    values('{titulo}', '{fecPublicacion}', '{isbn}', '{autor}')'''
    
    def traerLibros():
        conn = db()
        query = f"select * from Libros"
        return conn.consultarBDD(query)
    
    def traerLibros():
        conn = db()
        query = f"select * from Libros where nombre"
        return conn.consultarBDD(query)

