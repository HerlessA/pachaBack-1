1. `python -m venv venv`
2. `source venv/Scripts/activate`
3. `pip install Flask`
4. Crear file `entrypoint.py`

   - config file

5. Crear carpeta `app`

   - crear file `__init__.py` , para iniciar la app y configurar el proyecto (ejm: db, login, environments, ORM, error, etc. ).
   - crear carpeta `templates`, para mostrar vista html de base, error 500, 404, otros.
   - crear carpeta `static`, para estilos CSS

6. Crear carpeta `config`, necesario para definir los ambientes: prod, dev, testing, staying.

   - Crear DB en PostgreSQL, para dev
   - Crear DB en online en ElephantSQL, para prod (copiar url iniciando con: _postgresql:..._)

7. Crear carpeta `intance`

   - Crear file `config.py` y `config-testing.py`
   - Crear DB en PostgreSQL para testing

8. `pip install flask_login`
9. `pip install flask-sqlalchemy` (ORM)

---

### Modularización, con Blueprints

Crear módulos dentro de **carpeta `app` :**

10. Crear carpeta `auth`, para config todo lo relacionado a usuarios.

    - Crear file `__init__.py`, config Blueprint.
    - Crear carpeta `templates` y files html necesarios (login, registro, etc).
    - Crear file `models.py`, config estructura del usuario y métodos, para modelo de datos.
    - Crear file `forms.py` y `pip install flask_wtf`, config lógica de forms.
    - Crear file `routes.py`, para config rutas y métodos https.

11. Crear carpeta `public`, para config inf pública.

    - Crear file `__init__.py`, config Blueprint.
    - Crear carpeta `templates` y files html necesarios (index, etc).
    - Crear file `routes.py`, para config rutas y métodos https.

12. Crear file `models.py`, para nuevos modelos.

    - Crear files html de modelos dentro de carpeta public en `templates`.

13. Crear carpeta `product`, para config todo lo relacionado a productos.

    - Crear file `__init__.py`, config Blueprint.
    - Crear carpeta `templates` y files html necesarios.
    - Crear file `forms.py` y `pip install flask_wtf`, config lógica de forms.
    - Crear file `routes.py`, para config rutas y métodos https.

---

### Pruebas

Verificar instalación de:

- `pip install psycopg2`
- `pip install email_validator`
- `pip install slugify`

14. Correr en terminal:

    - `python entrypoint.py`
    - `flask shell` --> db.create_all() --> Salir: `Ctrl + z` + enter.
    - `flask run`
