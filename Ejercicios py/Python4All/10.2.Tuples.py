#Escribe un programa que lea atraves de mbox-short.txt y descubra la distribucion por hora del dia por cada uno de los mensajes, puedes colocar la hora de la linea "From " encontrando el timepo y asi divinendo el string usando un colo.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Una vez que hayas acumulado las cuentas por cada hora, imprime el contreo ordenado por hora 

filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
file = open(filename)

count = dict()

for line in file:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        count[line]= count.get(line,0)+1

lst=list()        
for value,count in count.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)