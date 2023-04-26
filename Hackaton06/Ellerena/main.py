from conexion import conexion

conexion = conexion()
query = "Select * from clientes;"
datos = conexion.consultarBDD(query)
print(datos)