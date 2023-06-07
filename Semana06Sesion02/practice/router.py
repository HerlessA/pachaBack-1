from database import cadena_conexion


def obtenerUsuario():
    conn = cadena_conexion()
    cursor = conn.cursor()
    sql_query = "SELECT * FROM usuario"
    cursor.execute(sql_query)
    result = cursor.fetchall()  # trae valores de tabla dentro de lista []
    # result = cursor.fetchone() #trae datos de un solo usuario
    # return result

    # transformar de una lista a un diccionario
    print("este es nuestro cursor: ", cursor.description)
    columnas = [columna[0] for columna in cursor.description]  # encabezados de tablas
    resultado = [dict(zip(columnas, fila)) for fila in result]
    print("Resultado: ", resultado)
    return resultado


def eliminarUsuario(id):
    conn = cadena_conexion()
    cursor = conn.cursor()
    sql_query = "delete from usuario where id = %s"
    cursor.execute(sql_query, (id,))
    conn.commit()
    return "Eliminado correctamente."


def crearUsuario(name, email):
    conn = cadena_conexion()
    cursor = conn.cursor()
    sql_query = "INSERT INTO usuario(nombre, correo) VALUES ('%s', '%s')"
    cursor.execute(
        sql_query,
        (
            name,
            email,
        ),
    )
    conn.commit()
    count = cursor.rowcount
    return count, "Creado correctamente"
