import psycopg2
from psycopg2 import Error


class db:
    def db(self):
        try:
            conn = psycopg2.connect(
                user="postgres",
                password="pSecret6#",
                host="127.0.0.1",
                port="5432",
                database="biblioteca",
            )
            return conn
        except Error as error:
            print(f"Ha ocurrido en error: {str(error)}")
            return False

    def consultarBDD(self, query):
        try:
            db = self.db()
            cur = db.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except Error as error:
            print(f"Ha ocurrido un error: {str(error)}")
            return False
        finally:
            if db:
                cur.close()
                db.close()

    def ejecutarBDD(self, query):
        try:
            db = self.db()
            cur = db.cursor()
            cur.execute(query)
            db.commit()
            exito = True
            return exito
        except Error as error:
            print(f"Ha ocurrido un error: {str(error)}")
            return False
        finally:
            if db:
                cur.close()
                db.close()
