# Ejercicio_1_LV
Ejercicio de Automatización E2E - Ejercicio 1

# Solución 
Para el desarrollo del ejercicio se usan técnicas de Web Scraping con Python con playwright.

# Lo que hace

Es un proyecto de Python que usa un archivo .json donde se coloca una lista de usuarios a modificar junto con el nuevo nombre. 

El proyecto guarda un archivo de logs y reporte que indica con fecha y hora los errores encontrandos junto con las actualizaciones realizadas.

# Instrucciones para montar ambiente
La versión de Python tiene que ser mayor o igual a 3.10

La libreria playwright es de versión 1.55.0

Se debe clonar el repositorio y con CMD abrir la ruta local donde se descargó el proyecto.

        cd C:\Users\USUARIO\Documents\ruta_local\

Para armar un ambiente virtual de python se puede correr los siguientes comandos en un CMD:

        python -m venv venv

        .\venv\Scripts\activate

Para instalar dependencias se corre en CMD:

        pip install -r requirements.txt

Para instalar los navegadores que usa playwright se ejecuta en el CMD:

        playwright install

Para ejecutarlo se corre el script logica.py

        python logica.py

# Parametros

El script parametros.py tiene variables o parámetros de configuración como: 
    
    La URL del sitio
    Referencias para ubicar los datos del .json 
    Bandera para configurar si se corre en primer plano (navegador se carga) o segundo plano (navegador no se carga).

# Credenciales

Contiene usuario y contraseña del sistema

# Archivo .json

Este tiene una clave llamada "prueba_orange" la cual acota al ejercicio 1 y deja abierto a poder configurar nuevos procesos.

Contiene una lista de usuarios a actualizar junto con sus nuevos nombres, facilita configurar este archivo y hacer actualizaciones masivas. 

    {
      "prueba_orange":
         [
           {
            "usuario_actual": "Jasmine.Morgan",
            "usuario_nuevo": "Jasmine.Morgan.Test"
           },
           {
            "usuario_actual": "dororeore",
            "usuario_nuevo": "Nuevo_valor"
           },
           {
            "usuario_actual": "Kukis5",
            "usuario_nuevo": "Kukis5.Test"
           }
         ]
    }

# Ejemplo resultado 

    2025-11-08 00:14:01 - INFO - ----------------INICIO PROCESO DE ACTUALIZACION DE USUARIOS----------------
    2025-11-08 00:14:02 - INFO - El proceso corre en segundo plano
    2025-11-08 00:14:09 - INFO - Se tiene 3 usuarios para actualizar
    2025-11-08 00:14:09 - INFO - El usuario Admin inicio sesion
    2025-11-08 00:14:40 - ERROR - 1. No existe el username Jasmine.Morgan
    2025-11-08 00:15:10 - ERROR - 2. No existe el username dororeore
    2025-11-08 00:15:12 - ERROR - 3. Kuk debe tener al menos 5 caracteres
    2025-11-08 00:15:12 - INFO - Se actualizaron 0 correctamente y fallaron 3
    2025-11-08 00:15:12 - INFO - ----------------FIN PROCESO DE ACTUALIZACION DE USUARIOS----------------


