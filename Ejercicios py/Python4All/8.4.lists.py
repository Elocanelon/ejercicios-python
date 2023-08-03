#Abre el archivo romeo.txt y leelo linea por linea, por cada linea, divide la linea en una list de palabras, usando metodo split(). El programa debe construir una lista de palabras por cada palabra en cada linea, chequeda si al palabra esta tomada in la listas y si no, agregala en la lista. Cuando el programa se complete, ordenalo e imprime el resultado words en python sort() como se observa en la salida deseada

filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "romeo.txt"

file = open(filename)
lst = list()
for line in file:
    words = line.rstrip().split()

    for element in words:
        if element in lst:
            continue
        else: 
            lst.append(element)
        
lst.sort()
print(lst)
            

