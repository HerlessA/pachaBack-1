from orator import DatabaseManager, Schema

DATABASES = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'a0973286',
        'user': 'postgres',
        'password': 'S4r4yCh1qu1',
        'prefix': ''
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
