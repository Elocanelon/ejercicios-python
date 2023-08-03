#Escribe un programa que lea a travez de mbox-short.txt y descubra quien ha enviado el mayor numero de correos. El programa debe buscar lineas con "From " t tomar la segunda palabra de esas lineas como la persona que envio el correo. EL programa creara un dictoonary que mapee el correo de envio a una cuenta por el numero de veces que aparezcan en el archivo. Despues que el dictionary se produzca, el programa leera a traves del dictionary usando un bucle maximo para buscar el mayor enviador

filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
file = open(filename)
lst = list()

for line in file:
    if not line.startswith("From "):
        continue
    line = line.split()
    lst.append(line[1])

count = dict()

for word in lst:
    count[word] = count.get(word, 0) + 1

countword = 0
countnumber = 0
for word, counts in count.items():
    if countnumber is None or counts > countnumber:
        countnumber = counts
        countword = word


print(countword, countnumber)