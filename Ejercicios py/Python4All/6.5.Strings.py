#Escribe codigo usando find() y string slicing para estraer el numero al final de la linea debajo. Concierte el valor extraido en un numero flotante e imprimelo

text = "X-DSPAM-Confidence:    0.8475"
text1 = text.find(":")
text2 = text[text1+1:]
text3 = float(text2)

print(text3)
