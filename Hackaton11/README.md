# HACKATHON SEMANAL

## MÓDULO 5: DESARROLLO Y PUBLICACIÓN DE NUESTRA API REST

### SEMANA 11
LOGRO: crea servicios RestAPI para un minimarket utilizando los conocimientos adquiridos en bases de datos, POO, Flask, JWT y PythonDotenv.

### I.	Es hora de demostrar lo aprendido:
Resuelve este reto aplicando lo aprendido en las semanas anteriores.  

### II.	Insumos para resolver el Reto:
-	Base de datos MongoDB o PostgreSQL
-	POO
-	Flask
-	JWT

Además:
-	Se debe realizar la estructura para nuestra BD
-	Se debe tener instalado Python
-	Se debe crear nuestro entorno virtual y configurar pylint
-	Se debe instalar los paquetes necesarios (si vamos a usar Mongo o PostgreSQL como base de datos)
-	Se debe crear nuestra interfaz por consola de python
-	Se debe usar POO para el desarrollo de la solución

### III.	Pasos a seguir para resolver el Reto:

-	Se tiene un requerimiento donde se debe crear una aplicación para un minimarket, donde se tendrá usuarios para cada rol específico: 
    -	Administrador
    -	Cajero
    -	Almacén

-	Para ello se debe tener categorizado cada producto, teniendo un stock y un precio (esto es algo relativo, ya que pueden presentarse más campos). 

-	Luego de ello, tenemos el uso de la aplicación que por cada módulo se debe restringir por acceso.

Debemos tener lo siguiente: 
    -	Almacén, se encarga de actualizar la data de los productos
    -	Cajero, se encarga de poder recibir los productos a comprar por el cliente y realizar la factura o boleta respectiva
    -	Administrador, podrá ver los productos (sin hacer cambios) como ver el reporte de las ventas del día o mes

-	Para poder realizar la facturación se debe recurrir al IGV, para ello debemos consumir el siguiente servicio: 
http://reto11.free.beeceptor.com
Este api nos devolverá el igv actual en el Perú.

-	 El requerimiento neto del sistema es crear un Módulo adicional para los usuarios (compradores), la funcionalidad es la siguiente: 
    -	Si es un cliente nuevo, se debe de crear su usuario al momento de realizar su primera compra (al pagar)
    -	Si el usuario ya existe, solo se debe tomar su usuario para insertar el identificador para guardar el historial de su compra
    -	Gracias a ello el usuario podrá ver el historial de sus compras realizadas día a día

### IV.	Descripción del Reto
Los estudiantes deberán crear servicios RestAPI para un minimarket utilizando los conocimientos adquiridos en bases de datos, POO, Flask, JWT y PythonDotenv. 

### V.	Solución del Reto
Para que el reto esté cumplido al 100% deberás tener cubiertos los requisitos básicos expuestos:

-	Tener un crud completo para los módulos de almacén, cajeros, administradores y usuarios
-	Validar que se puedan cumplir los roles con sus funciones determinadas
-	Validar que se pueda obtener un reporte con filtros en el que se puedan manejar los requests
-	Tener el historial de compras manejándose por filtros para el usuario

### VI.	Presentación del Reto
-	El documento debe ser presentado de manera individual o grupal (según se coordine con el docente)
-	El tiempo de cada presentación lo definirá el docente a cargo

### VII.	Feedback
-	El docente dará feedback a los estudiantes sobre los ejercicios realizados