# Django - postgreSQL

https://docs.djangoproject.com/en/4.2/intro/tutorial02/

https://docs.djangoproject.com/en/4.2/intro/tutorial03/

## Initial setup:

1. `python -m venv venv`
2. `source venv/Scripts/activate`
3. `python -m pip install Django`
4. Verifying in terminal: `python` -> >>> import django -> >>> print(django.get_version())

   ctrl + z + enter

5. Creating a project: `django-admin startproject projectName .`

   ( "." goes to no create two folders with same name.)

6. The development server: `python manage.py runserver`

7. Set up _setings.py_ folder:

   - TIME_ZONE = "UTC" - LANGUAGE_CODE = "en-us"

   - TIME_ZONE = "America/Lima" - LANGUAGE_CODE = "es-pe"

   - DATABASES = {...} _Set up all about db_ to use for the project.

   - ALLOWED_HOSTS = [] It could be empty or insert code about conections On-premise or Cloud.

   - MIDDLEWARE = [] config middlewares like login systems, ...

   - TEMPLATES = []

## Database setup:

1. `pip install psycopg2`

2. `python manage.py migrate`

3. `python manage.py createsuperuser`

   -> name -> email -> password

4. `python manage.py runserver`
5. Go to: http://127.0.0.1:8000/admin -> insert user credentials (name and psw).

## App setup:

There will be many apps in a project.

1. `python manage.py startapp appName`

   exp: python manage.py startapp polls -> polls folder is created.

2. Setup `settings.py` file in project folder (Blog). Add app.

   ```
   INSTALLED_APPS = [
    ...,
    "polls.apps.BlogConfig",
   ]
   ```

3. Set up `urls.py` file inside app folder.

   Set up

4. Create `urls.py` file inside app folder.

   Set up

5. Set up _urlpatterns_ project/urls.py file:

   ```
   urlpatterns = [
    path("polls/", include("polls.urls")),...
   ]
   ```

6. Setup `models.py` file in app folder (polls).

   Model is an object. It will save in db.

7. Create migration: `python manage.py makemigrations appName`

8. Migrate: `python manage.py migrate`

9. Register models in `admin.py` file.

10. Create _template/polls_ folder and inside _fileNme.html_ files.

    Insert templates.

11. Run server: `python manage.py runserver`

    Verify by creating a new poll.

    <!-- _Repeat 4, 5, 7 if there are changes._ -->

**notes:**

- If show an error as: str objr_str, transformar a string.
- If migrations failed, try deleting that folder and repeat the steps.
