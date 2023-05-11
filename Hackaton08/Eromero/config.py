from orator import DatabaseManager, Schema
import psycopg2

config = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'a0973286',
        'user': 'postgres',
        'password': 'S4r4yCh1qu1',
        'prefix': ''
    }
}

db = DatabaseManager(config)
schema = Schema(db)
