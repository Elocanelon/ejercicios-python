#Escribe un programa que procese el nombre de un archivo, entonces abra ese archivo y lea atraves del archivo, buscando las lines de la form
#X-DSPAM-Confidence: 0.8485
#Cuenta esas lineas y extrae los valores flontantes por cada una de las lineas y calcula el promedio de esos valores y produce una salida como se muestra debajo. No uses la function sum or una variable llamada sum en tu solucion 

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lineCount = line.find("0")
    number = float(line[lineCount:])
    count = count + 1
    total = total + number 
    
    average = total / count
print("Average spam confidence:", average )



