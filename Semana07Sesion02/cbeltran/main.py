import conexion

conn = conexion.conexion("mongodb://localhost:27017","sesion02")

class Mobile: 
    def __init__(self, nombre, marca, modelo):
        self.nomobre = nombre
        self.marca = marca
        self.modelo = modelo
    
    def toDic(self):
        return{
            "nombre":self.nomobre,
            "marca":self.marca,
            "modelo":self.modelo
        }

equipo = Mobile("Iphone", "Apple", "13 Pro")

#conn.insertar_registro("producto",equipo.toDic())

print(conn.actualizar_registro("producto",{"modelo":"13 Pro"},{"nombre":"Galaxy"}))
#print(conn.obtener_registro("producto",{"modelo":"13 Pro"}))