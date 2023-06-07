from psycopg2 import connect

host = "0.0.0.0"
port = 5432
dbname = "prueba"
user = "postgres"
password = "12demetrio34"


def cadena_conexion():
    conexion = connect(
        host=host, port=port, dbname=dbname, user=user, password=password
    )

    return conexion
