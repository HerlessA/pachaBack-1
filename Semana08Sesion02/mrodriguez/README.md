Comandos

1. pip install --upgrade pip wheel

2. pip install wheel

3. pip install httpie

4. pip install flask flask-orator
   flask-swagger-ui (para facilitar visibilidad en cosultas front)

5. pip install pysycop2

6. crear file app.py
   configurar ORM, conexion a postgres
   probar corriendo: python app.py

7. crear BD en postgres

8. crear file db.py
   config cli, para conectar db con orator

9. CREANDO MIGRACIONES
   python db.py make:migration create_users_table --table users --create
   genera una carpeta migrations, dentro file de nombre fecha+nombreDeTabla
   Este file se llama migración
   Editar/configurar file generado en migrations, tambien configurar foreign keys si corresponde.
   (luego se recomienda crear seeders, para tener data de prueba)

10. Ejecutar MIGRACION
    python db.py migrate
    yes
    Se crea la tabla en postgres más migraciones
    Para ver el estado, si se creó:
    python db.py migrate:status

11. CREAR MODELOS en app.py
    probrar con: python app.py, que corra localhost

12. En otro terminal activar venv y correr la librería para conectar al http

13. POST
    http POST http://127.0.0.1:5000/users name=twittor email=twittor@twittor.com
    Si en caso sale error, probrar en postman desktop si se ejecuta el request

14. GET
    (PARA TRAER USER ID = 1)
    http http://127.0.0.1:5000/users/1

    (PARA TRAER USERS)
    http http://127.0.0.1:5000/users

15. PATCH
    (PARA ACTUALIZAR UN CAMPO USER ID = 1)
    http PATCH http://127.0.0.1:5000/users/1 name="Anómino"

16. DELETE TODA LA DATA
    python db.py migrate:refresh
    yes
    reinicia la data (borra toda la info)

17. DELETE
    Ejm: mensaje por su id
    http DELETE http://127.0.0.1:5000/messages/4

18. CREANDO SEEDERS
    SEEDER: es una data que se puede precargar. Ejm: para iniciar pruebas crud. (Siliar a moks en js)
    Inicializar con:
    python db.py make:seed users_table_seeder
    crea seeds carpeta, con files llamados: nombreDeTablaDelSeeder.py y otro db_seeder.py
    configurar files

19. Ejecutar SEEDER
    Antes aplicar paso 16
    python db.py db:seed
    yes
    Se cargan los datos en postgres

**nota**: para interactuar se debe estar ejecutando localhost en segundo plano.

    para ver swagger dar /swagger a localhost
