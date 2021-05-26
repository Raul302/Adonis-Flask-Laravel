1.- Crear una base de datos de postgres llamada "bdExample"
modificar el archivo .env contenido en las carpetas "appExample" y "appLaravelExample" y en "Apis" buscar el archivo main.py y modificar el metodo "conexion" en la linea 9 con las credenciales
con los siguientes datos ó con sus propias credenciales,cambiar la contraseña por la utilizada para conectarse a postgres : 

DB_CONNECTION=pgsql
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE=bdExample
DB_USERNAME=postgres
DB_PASSWORD=abril302


2.- entrar a la carpeta "appLaravelExample",hacer un composer install,y correr las migraciones
con php artisan migrate


3.- correr el servicio dependiendo de la carpeta : 
"appLaravelExample" --> php artisan serv

"appExample" ---->adonis serv

"Apis" ----> python main.py
# Adonis-Flask-Laravel
