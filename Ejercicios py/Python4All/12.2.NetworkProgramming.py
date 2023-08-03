#Recopila numeros desde HTML usando BeautifulSoup en esta tarea, escribiras un programa de python, Est pograma usara urllib para leer el HTML desde los archivos de data debajo, y analizara la data, extrayendo los numeros y calculando la suma de los numeros in el archivo.

#Data ejemplo: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Data actual: http://py4e-data.dr-chuck.net/comments_1853661.html (Sum ends with 13)

from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("http://py4e-data.dr-chuck.net/comments_1853661.html").read()
soup = BeautifulSoup(url, "html.parser")
tags = soup("span")

sum = 0 
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
