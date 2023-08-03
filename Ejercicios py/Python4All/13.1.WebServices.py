#En esta asignacion escribiras un programa de python que analice un url, lea la data XML de ese url usando urllib y despues analice y extraiga las cuentas de comentarios de la data xml, calcule la suma de los numeros en el archivo. 

#Data ejemplo http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Data Actual: http://py4e-data.dr-chuck.net/comments_11961.xml (Sum ends with 89)

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
if len(url) < 1:
    url = ""

print ("Retrieving", url)

total = 0
count = 0

data = urllib.request.urlopen(url).read()
print("Retrieving", len(data), "characters")

tree = ET.fromstring(data)
lst = tree.findall("comments/comment")

for item in lst:
    count = count + 1
    text_count = item.find("count").text
    total = total + float(text_count)

print("Count: ", count)
print("Sum: ", total)