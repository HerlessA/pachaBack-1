# Conexión Python con PostgreSQL

## Creando entorno

Necesario para trabajar en distintos proyectos y/o
no generar conflictos si tienen distintas versiones.

1. Verificar version python y pip

   `python --version`

   `pip --version`

   _nota_: si en caso no tiene pip instalar

   `python -m pip install --upgrade pip`

2. Crear entorno:

   `python -m venv env` (genera un file env)

   o

   `python -m venv venv` (genera un file venv) (**OK**)

3. Verificar:
   `source venv/`

4. Activar scripts: _aparece (venv o env debajo)_

   `source env/Scripts/activate` o

   `source venv/Scripts/activate`

5. Crear file requirements.txt: _(opcional)_

   Escribir lista de paquetes necesarios para el proyecto, que se instalaran luego.

   Esto ayuda a tener mejor detallado los paquetes necearios para ejecutar el proyecto,
   si cambio a otro ordenador u otra persona necesita ejecutarlo.
   También porque el file env puede pesar demasiado y solo necesitaría llevar
   requirements.txt.

6. Instalar paquetes:

   - Del file requirements.txt:

   `pip install -r requirements.txt`

   Verificar con: `pip list` o

   `pip freeze` para ver paquetes del entorno.

   - Directamente:

   `pip install nombreDelPaquete`

   _nota:_ para ver puertos activados correr: `netstat -a`

7. Conectar con base de datos, crear files.py y codigo respectivo.

   _nota:_ para correr en bash:

   `python nameFile.py`

   **Si no generé file requirements y necesito saber cuales fueron**

   `pip freeze > requirements.txt`

8. Desactivar entorno con: `deactivate`

## PAQUETES RECOMENDADOS:

- **pysycon2**, para conectar a BD postgres
- **tabulate**, para dar formato con rejillas en tabla.
