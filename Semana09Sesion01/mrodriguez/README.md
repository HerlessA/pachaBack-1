Comandos usados:

- python -m venv venv

- source venv/Scripts/activate

- pip install Flask

- pip install -r requirements.txt (si hay librerías)

- pip freeze > requirements.txt (exportar libs en txt)

- export FLASK_APP="app.py"

- flask run

## Renderizando una página HTML

Jinja2

Flask trae por defecto un motor de renderizado de plantillas llamado Jinja2 que te ayudará a crear las páginas dinámicas de tu aplicación web.

Para renderizar una plantilla creada con Jinja2 simplemente hay que hacer uso del método:

`render_template("nombreFile", variable=valor)`

## Librerías para formularios

- Flask-WTF: para heredar campos/elems html
- email-validator
- flask-login : almacena user id, retringe accesos, etc.

## sqlalchemy - ORM para Flask

- `pip install flask-sqlalchemy`

- psycopg2: para conectar a DB postgreSQL

## Creando la base de datos

1.  `python`
2.  `from app import db` -> db.create_all()
