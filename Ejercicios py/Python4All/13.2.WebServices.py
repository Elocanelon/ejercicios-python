#En esta asignacion escribiras un programa python que analaizara por un URL, leer la data JSON de esa url usando urllib y analice y extraiga los cuentas comentadas de la data JSON, calcule la suma de los numeros y sume los numeros en los archivos con la suma debajo 

#Proveemos de dos archivos en esta tarea, una es un simple archivo donde te damos la suma para tus pruebas y en otro es donde la data actual donde necesitas procesar por la tarea

#data de ejemplo http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#data actual: http://py4e-data.dr-chuck.net/comments_1853664.json (Sum ends with 58)

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request
import json

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"
print("Retrieving", url)

data = urllib.request.urlopen(url)
raw = json.loads(url.read().decode)

print("Retrieved", len(str(raw)), "characters")

data = raw.get("comments")

num = 0
total = 0
for i in range(len(data)):
    tmp = data[1]
    value = tmp.get("count")
    num = num + 1 
    total = total + int(value)
print("Count: ", num)
print("Sum: ", total)
