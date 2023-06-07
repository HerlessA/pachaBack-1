from psycopg2 import connect

# conexion a base de datos
host = "127.0.0.1"  # 0.0.0.0
port = 5432
dbname = "prueba"
user = "postgres"
password = "pSecret6#"


def cadena_conexion():
    conexion = connect(
        host=host, port=port, dbname=dbname, user=user, password=password
    )
    return conexion
