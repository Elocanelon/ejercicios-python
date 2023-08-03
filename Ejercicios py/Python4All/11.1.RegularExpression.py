#En esta asignacion, leeras atraves y analizaras un archivo con texto y numeros. Extraeras todos los numeros en un archivo y calcularas la suma de los numeros

#Data de ejemplo: http://py4e-data.dr-chuck.net/regex_sum_42.txt (hay 90 valores con una suma=445833)

#Data actual: http://py4e-data.dr-chuck.net/regex_sum_1853659.txt (Hay 102 valores y una suma que termina en 245)

import re 

filename = filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "regex_sum_data.txt"
file = open(filename)

calc = list()
count = 0

for line in file:
    line = line.rstrip()
    words = re.findall("[0-9]+", line)
    for numb in words: 
        count += 1
    calc = calc + words

sum = 0 
for bigsum in calc:
    sum = sum + int(bigsum)

print("There are", count, "values and the sum =", sum)

