from psycopg2 import connect

host = "localhost"
port = 5433
dbname = "school"
user = "postgres"
password = "021087Mikeyla"

def cadena_conexion():
    conexion = connect(host = host, port = port, dbname = dbname, user = user, password = password)

    return conexion