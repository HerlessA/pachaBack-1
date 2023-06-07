from database import cadena_conexion


def obtenerUsuario():
    conn = cadena_conexion()
    cursor = conn.cursor()
    sql_query = "select * from usuario"
    cursor.execute(sql_query)
    result = cursor.fetchall()

    # transformar de una lista a un diccionario
    print("este es nuestro cursor: ", cursor.description)
    columnas = [columna[0] for columna in cursor.description]
    resultado = [dict(zip(columnas, fila)) for fila in result]
    print("Resultado: ", resultado)
    return resultado


def eliminarUsuario(id):
    conn = cadena_conexion()
    cursor = conn.cursor()
    sql_query = "delete from usuario where id_usuario = %s"
    cursor.execute(sql_query, (id,))
    conn.commit()
    return "Eliminado Correctamente!! "
