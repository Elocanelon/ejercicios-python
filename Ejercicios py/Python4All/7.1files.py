#Escribe un programa que lea un archivo e imprima todo el contenido (linea por linea) en mayusculas 

filename = input("Enter file name")
if len(filename) < 1:
    filename = "mbox-short.txt"
file = open(filename)

for line in file:
    words = line.rstrip()

    print(words.upper())