#En esta asignacion, escribiras un programa de python que expanda en ttp://www.py4e.com/code3/urllinks.py. El programa usara urllib para leer el HTML desde los archivos de data debajo, extrae los valores href= desde el anchor tag, scaea por un tag que esta en una particular posicion relatvia del primer nombre en la lista, devuelve ese link y repite el proceso por un numero de veces y reporta el ultimo apellido que conseguiste.

#Ejemplo: Comienza en http://py4e-data.dr-chuck.net/known_by_Fikret.html.
#Consigue el link en la posicion 3 (el primer nombre es 1). Sigue ese link, repite este proceso 4 veces. La respuesta es el ultimo nombre que tu recibiste. 
# Secuencia de nombres ikret Montgomery Mhairade Butchi Anayah
# Ultimo nombre en secuencias: Anayah
#Problema actual: Comienza en http://py4e-data.dr-chuck.net/known_by_Juniper.html.
# Encuentra el link en la posicion 18 (el primer nombre es 1). Sigue ese link, repite ese proceso 7 veces. La respuesta es el ultimo apellido que recibiste
#Pista: El primer caracter de el nombre de la ultima hoja que vas a cargar es: Y


import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = int(input("Enter Count: "))
position = int(input("Enter position: "))-1
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
href = soup("a")

for i in range(count):
    link = href[position].get("href", None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
