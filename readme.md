# PROYECTO DE BREWERY (pero ahora con Flask y backend)

## Indice

- [Ejecutar de manera local - orientado a linux](#ejecutar-de-manera-local---orientado-a-linux)
    - [Creacion de entorno virtual](#creacion-de-entorno-virtual)
    - [Configuracion de la Base de Datos](#configuracion-de-la-base-de-datos)
    - [Configuracion de TailWind](#configuracion-de-tailwind)
    - [Fin de la configuracion](#fin-de-la-configuracion)
- [Diseño UI](#diseño-ui)
    - [Home](#home)
    - [Catalogo](#catalogo)
    - [Compras](#compras)
    - [Seccion ADMIN](#seccion-admin)
    - [Login](#login)
    - [Registro](#registro)


# Ejecutar de manera local - orientado a linux
Al ser un micro framework, Flask es tan liviano y simple que hacerlo andar de manera local se logra ejecutando unos pocos comandos de consola

`REQUISITOS:` El proyecto requiere que en su equipo contenga configuradas e instaladas las siguientes tecnologias **Python 3, GIT, MySQL, Node.js**

1. **Crear una carpeta** en donde vamos a ejecutar este proyecto de manera local
2. Abrir una **consola** de comandos y **posicionarse dentro de la carpeta** contenedora del proyecto Flask
3. En la consola **ejecutar** los sigueintes comandos:
~~~ bash
git clone https://github.com/pala83/Brewery-flask.git
cd Brewery-flask
~~~

## Creacion de entorno virtual
4. Cree un entorno virtual y luego activelo:
~~~ bash
python3 -m venv venv
source venv/bin/activate
~~~
Para desactivarlo ejecute el comando `deactivate`

5. Instale las dependencias del proyecto:
~~~
pip install -r requirements.txt
~~~
## Configuracion de la Base de Datos
Este proyecto fue implementado utilizando **MySQL** y la estructura general de la base de datos que debe copiar y pegar en su base de datos local esta en el arhivo `database/brewery.sql`, la base de datos no tiene datos ya que la intencion de esta guia es que pueda dejar funcionando el CRUD y utilizarlo como desee, tampoco se tomaron medidas de seguridad basicas con los datos sensibles de la base de datos, ya que es un proyecto con fines academicos y no fue implementado con la intencion de hacerle un Deploy.

6. Cargue los datos del archivo `database/brewery.slq` en su base de datos MySQL
7. Configure la base de datos con los datos pertinentes de su sistema en el archivo `src/models/model.py`
~~~ py
# Configuracion por default si es que usa XAMPP y PHPMyAdmin
app.config['MYSQL_DATABASE_HOST'] = '' # Default = 'localhost'
app.config['MYSQL_DATABASE_USER'] = '' # Default = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # Default = ''
app.config['SECRET_KEY'] = 'codoacodo'
~~~

## Configuracion de TailWind
El **frontend** del sistema esta implementado en TailwindCSS, este framework de css se compila a CSS3 para poder trabajar de forma mas prolija y organizada.
8. Instalar TailwindCSS
~~~
npm install -D tailwindcss
~~~
9. Active el interprete de Tailwind y para continuar va a necesitar otra consola
~~~
cd src/
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
~~~

## Fin de la configuracion
Ya esta todo el proyecto configurado, ahora solo debe ejecutar el siguiente comando y abrir la aplicacion en el navegador
10. Si esta en su nueva consola por el paso anterior, posicionese en la carpeta `Brewery-flask` y ejecute los siguientes comandos
~~~
source venv/bin/activate
python3 src/app.py
~~~

# Diseño UI
La UI fue diseñada con TailwindCSS, tiene tema claro, tema oscuro y es totalmente responsive con enfoque mobile first, todo esto lo facilita Tailwind de forma nativa.

## Home
| Breackpoint | Dark                                           | Light                                                      |
|-------------|------------------------------------------------|------------------------------------------------------------|
| LG: 1024    | ![Breackpoint 1024](assets-readme/Home-lg.png) | ![Breackpoint 1024 light](assets-readme/Home-lg-light.png) |
| MD: 768     | ![Breackpoint 768](assets-readme/Home-md.png)  | ![Breackpoint 768 light](assets-readme/Home-md-light.png)  |
| SM: 480     | ![Breackpoint 480](assets-readme/Home-sm.png)  | ![Breackpoint 480 light](assets-readme/Home-sm-light.png)  |

## Catalogo

## Compras

## Seccion ADMIN

## Login
| Breackpoint | Dark                                           | Light                                                        |
|-------------|-------------------------------------------------|-------------------------------------------------------------|
| LG: 1024    | ![Breackpoint 1024](assets-readme/Login-lg.png) | ![Breackpoint 1024 light](assets-readme/Login-lg-light.png) |
| MD: 768     | ![Breackpoint 768](assets-readme/Login-md.png)  | ![Breackpoint 768 light](assets-readme/Login-md-light.png)  |
| SM: 480     | ![Breackpoint 480](assets-readme/Login-sm.png)  | ![Breackpoint 480 light](assets-readme/Login-sm-light.png)  |

## Registro
| Breackpoint | Dark                                               | Light                                                          |
|-------------|----------------------------------------------------|----------------------------------------------------------------|
| LG: 1024    | ![Breackpoint 1024](assets-readme/Registro-lg.png) | ![Breackpoint 1024 light](assets-readme/Registro-lg-light.png) |
| MD: 768     | ![Breackpoint 768](assets-readme/Registro-md.png)  | ![Breackpoint 768 light](assets-readme/Registro-md-light.png)  |
| SM: 480     | ![Breackpoint 480](assets-readme/Registro-sm.png)  | ![Breackpoint 480 light](assets-readme/Registro-sm-light.png)  |