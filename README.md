# Proyecto Ingeniería de Software - "Ley Cholito"
## Plataforma de denuncias, gestión y adopción de animales

Este repositorio contiene el proyecto de Ingeniería de Software (CC-4401) de la FCFM. Este proyecto
esta centrado en resolver la problemática del manejo de denuncias relacionadas a la "Ley Cholito",
gestión por parte de las municipalidades de estas y resolver el cuidado de los animales rescatados con ONG's que tendrán la responsabilidad de cuidar y poner en adopción a estos animales.

## El proyecto esta estructurado de la siguiente manera:

 <pre>
|-- CholitoProject
|   |-- CholitoProject
|   |   |-- settings.py
|   |   |-- urls.py
|   |   `-- wsgi.py
|   |-- animals
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- templates
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|   |-- complaint
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- templates
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|   |-- manage.py
|	|-- media
|   |-- municipality
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- templates
|   |   |-- tests.py
|   |   |-- urls.py
|   |   `-- views.py
|	|-- static
|   |-- templates
|   `-- users
|       |-- admin.py
|       |-- apps.py
|       |-- models.py
|       |-- templates
|       |-- tests.py
|       |-- urls.py
|       `-- views.py
|-- README.md
`-- requirements.txt
</pre>

El proyecto principal se encuentra en la carpeta CholitoProject, que contiene las configuraciones globales del proyecto en ```settings.py```, las urls por defecto que mappeara django desde los request estarán en el archivo ```urls.py```.

Ademas se generan app's (animales, complaint, municipality, etc.) en sus carpetas respectivas. Cada una de estas tendrá consigo:
* templates : Carpeta que contiene los archivos html correspondientes a las vistas de la app.
* urls.py : Archivo que contiene las rutas y conexiones con las funciones respuestas.
* views.py : Archivo que contiene la lógica de respuestas a las peticiones.
* models.py : Archivo que contiene las clases que representan los objetos que el ORM de django mappeara y guardara en la base de datos.

Los estáticos del projecto estarán en la carpeta ```static```

Los archivos de carga/descarga del projecto estarán en la carpeta ```media```
## Requisitos del proyecto
Para la correcta ejecución de este proyecto se requiere python 3 y pip. 

## Instalación del proyecto

Para instalar y hacer correr esta plataforma se recomienda el uso de un ambiente virtual, herramientas como [virtualenv](https://virtualenv.pypa.io/en/stable/) o su [wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) son altamente recomendadas, primero se deben instalar las dependencias del proyecto señaladas en el archivo ```requirements.txt```, para esto se puede utilizar el comando 
``` pip install -r path/to/requirements.txt ```
 ya con esto solo debemos crear la base de datos, lo cual se puede hacer mediante los comandos
 ``` 
 django /path/to/manage.py makemigrations
 django /path/to/manage.py migrate
 ```

 