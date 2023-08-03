#Escribe un programa que repetidamente imprima un usario por numero hasta que el usaurio ingrese "done". imprima el valor mas alto y el mas bajo de los numeros. Si el usuario ingresa algo mas que un valor con un numero, atrapalo con un try/except e ingresa un mensaje apropiado e ignora el numero. Ingresa 7, 2, bob, 10, y 4 y vincula la salida debajo.

largest = None
smallest = None
while True:
    
    try: 
        num = input("Enter a number: ")
        if num == "done":
            break
        else:
            num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or largest < num:
        largest = num
    elif smallest is None or smallest > num:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
