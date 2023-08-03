#Escribe un programa para un puntaje entre 0.0 y 1.0, si el puntaje esta fuera de rango, imprime un error. Si el puntaje esta entre 0.0 y 1.0, imprime una nota usando la siguiente tabla 
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#Si el usuario ingrea un valor fuera del rango, imprime un mensaje de error adecuado y exit. Para el testeo, ingresa un puntaje de  0.85

note = input("Enter score: ")

try:
    grade = float(note)
except: 
    print("Score out of range, please enter a note between 0.0 and 1.0")

if grade > 1.0:
    print("Score out of range, please enter a note between 0.0 and 1.0")
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
elif grade < 0.6 :
    print("F")
elif grade < 0.0:
    print("Score out of range")
