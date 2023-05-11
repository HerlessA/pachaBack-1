from db import conexion
class Libros:
    def _init_(self, titulo, fecPublicacion, isbn, autor):
        self.titulo = titulo
        self. fecPublicacion = fecPublicacion
        self.isbn = isbn
        self. autor = autor

    def crearLibro(self):
        conn = conexion()
        query = f'''INSERT INTO public."Libros"(
	                titulo, "fecPublicacion", isbn, autor)
                    values('{self.titulo}', '{self.fecPublicacion}', '{self.isbn}', {self.autor})'''
        return conn.ejecutarBDD(query)
    
    def traerLibros():
        cn = conexion()
        query = f'''Select * from Libros'''
        return cn.consultarBDD(query)
    
    def traerLibro(self):
        cn = conexion()
        query = f'''Select * from Libros where titulo = {self.titulo}'''
        return cn.consultarBDD(query)
