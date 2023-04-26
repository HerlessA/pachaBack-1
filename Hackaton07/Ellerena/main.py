from conexion import Conexion

class Mobile:
    def __init__(self, nombre, marca, modelo):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo

    def ToDic(self):
        return{
            "nombre":self.nombre,
            "marca":self.marca,
            "modelo":self.modelo
        }


conn = Conexion("mongodb://localhost:27017","tarea02")




conn.insertar_registro("producto",equipo.ToDic())


condicion = {
    'marca': 'Android'
}
newvalues = { "$set": { 'marca': "Android" } }