# Estructura de un proyecto Flask. Blueprints

Aspecto importante que afecta al mantenimiento del proyecto, especialmente cuando trabajamos en equipo y crece en líneas de código.

https://j2logo.com/tutorial-flask-leccion-6-estructura-proyecto-flask-blueprints/

## Estructura recomendada

```
+ mi_proyecto/
   |_ app/
      |_ __init__.py
      |_ common/
      |_ mod1/
         |_ __init__.py
         |_ routes.py
         |_ templates/
            |_ mod1/
               |_ template1.html
               |_ template2.html
         |_ models.py
         |_ forms.py
         |_ ...
      |_ mod2/
         |_ __init__.py
         |_ routes.py
         |_ templates/
            |_ mod2/
               |_ template1.html
               |_ template2.html
         |_ models.py
         |_ forms.py
         |_ ...
      |_ ...
      |_ static/
         |_ css/
         |_ images/
         |_ js/
      |_ templates/
         |_ base_template.html
         |_ ...
   |_ config
      |_ development.py
      |_ local.py
      |_ production.py
      |_ testing.py
   |_ env/
   |_ fixtures/
   |_ instance
      |_ __init__.py
      |_ config.py
   |_ .gitignore
   |_ CHANGELOG.md
   |_ entrypoint.py
   |_ README.md
   |_ requirements.txt

```

## NOTAS

1. Python es un lenguaje semi-compilado o semi-interpretado.

   Un lenguaje interpretado o de script se ejecuta mediante un programa intermedio que se llama intérprete. Los lenguajes interpretados no se compilan a lenguaje de máquina para poder ejecutarse.

   A pesar de lo anteriormente tratado python posee características de lenguajes compilados y debido a estas características se puede decir que python es un lenguaje semi-interpretado. El script python se traduce a un lenguaje intermedio llamado bytecode que posee la extensión .pyc o .pyo (bytecode optimizado).

2. en cada carpeta de python, debe ir un file `__init__.py`

3. Considerar siempre tener dos ambientes:

   - Desarrollo: antes de pasar a producción, pasan a QA, staying.

   - Producción
