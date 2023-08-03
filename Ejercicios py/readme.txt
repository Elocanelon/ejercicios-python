*Para descargar Python*
Linux 
Generalmente en maquinas linux ya Python esta descargado por defecto, para verificar que sea el caso, abrir una terminal de comando e introducir el siguiente comando 

python --version

En el caso de contrario a traves de la terminal introduce los siguientes comando

-Maquinas ubutu y debian

sudo apt update *Para actualizar los paquetes de sistema*
sudo apt upgrade *Para descargar y actualizar todos los paquetes del sistema*

sudo apt-get install python3 *Para acutalizar ultima version de python*

-Maquinas redhat y derivados-
Aplicar comando yum:

sudo yum install python3

Windows
Puedes descargar Python para Windows desde la siguiente web https://www.python.org/downloads/windows/. Clica en el enlace "Latest Python 3 Release -Python x.x.x".
Después de descargar el instalador, deberías ejecutarlo (dándole doble click) y seguir las instrucciones.

Para ejecutar un archivo python, desde una terminal dirigirte al archivo .py que quieras ejecutar usando el comando cd y colocar el siguiente comando

python3 *nombreDelPrograma*.py

La base de datos usadas para los ejercicios de SQL es SQLite. 
para la instalacion se debe hacer un update y posteriormente instalar la base de datos 

sudo apt update
sudo apt upgrade
sudo apt install sqlite3
sudo apt install sqlitebrowser

