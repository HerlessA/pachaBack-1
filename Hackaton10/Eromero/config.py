from orator import DatabaseManager, Schema
import psycopg2

class OratorConfig:
    ORATOR_DATABASES = {
        'postgres': {
            'driver': 'postgres',
            'host': 'localhost',
            'database': 'a0973286',
            'user': 'postgres',
            'password': 'S4r4yCh1qu1',
            'prefix': ''
    }
}
    SECRET_KEY = "ANAMA23"


db = DatabaseManager(OratorConfig.ORATOR_DATABASES)
schema = Schema(db)

