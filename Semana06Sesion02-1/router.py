from database import cadena_conexion

def obtenerUsuario():
    conn = cadena_conexion()
    cursor = conn.cursor()
    sql_query= "select * from students"
    cursor.execute(sql_query)
    result = cursor.fetchall()


    print("este es nuestro cursor: ",cursor.description)
    columnas = [columna[0] for columna in cursor.description]
    resultado = [dict(zip(columnas, fila)) for fila in result] 

    print("Resultado: ", resultado)
    return resultado