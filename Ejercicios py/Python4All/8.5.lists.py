#Abre el archivo m-box-short.txt y leelo linea por linea, cuando consigas una linea que conmience con "From " como la linea siguiente:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Dividiras el From de la linea usando split() e imprimeras la segunda palabra en la linea(La direccion entera de la pérsiona que mando el mensaje) e imprimiras al final un conteo
#Pista: Asegurante de no incluir las lineas que comiencen con "From:", tambien mira en la ultima linea del ejemplo como debes imprimir el conteo.

filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
file = open(filename)
count = 0

for data in file:
    data.rstrip()
    line = data.split()

    if "From" in line:
        count = count + 1
        print(line[1])

print("There were", count, "lines in the file with From as the first word")

    