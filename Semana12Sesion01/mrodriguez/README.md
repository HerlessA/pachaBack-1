# Django

https://www.djangoproject.com/start/

## Initial setup:

1. `python -m venv venv`
2. `source venv/Scripts/activate`
3. `python -m pip install Django`

   https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-releas

4. Verifying in terminal: `python` -> >>> import django -> >>> print(django.get_version())

   ctrl + z + enter

5. Creating a project: `django-admin startproject projectName .`

   ```
   mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
   ```

_More info:_ https://docs.djangoproject.com/en/4.2/intro/tutorial01/

6. The development server: `python manage.py runserver`

7. _OPTIONAL:_ Change languaje (if you like): go to _setings.py_ folder.

   - TIME_ZONE = "UTC" - LANGUAGE_CODE = "en-us"

   - TIME_ZONE = "America/Lima" - LANGUAGE_CODE = "es-pe"

## Database setup:

1. `python manage.py migrate`

   _db.sqlite3_ file is created.

   (to visualize, install _SQLite Viewer_ from VSC).

2. `python manage.py createsuperuser`

   -> name -> email -> password

3. `python manage.py runserver`
4. Go to: http://127.0.0.1:8000/admin -> insert user credentials (name and psw).

## App setup:

There will be many apps in a project.

1. `python manage.py startapp appName`

   exp: python manage.py startapp blog -> blog folder is created.

2. Setup `settings.py` file in project folder (pachaqtec). Add app.

   ```
   INSTALLED_APPS = [
    ...,
    "blog.apps.BlogConfig",
   ]
   ```

3. Setup `models.py` file in app folder (blog).

   Model is an object. It will save in db.

4. Create migration: `python manage.py makemigrations appName`

5. Migrate: `python manage.py migrate`

6. Register model in `admin.py` file.

7. Run server: `python manage.py runserver`

   Verify by creating a new blog.

   _Repeat 4, 5, 7 if there are changes._

**notes:**

- If show an error as: str objr_str, transformar a string.
- If migrations failed, try deleting that folder and repeat the steps.
