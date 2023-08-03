#Escribe un programa para imprimir el usuario por horas y salario por hora usando un input para computar el pago. La paga por hora para las horas superior a 40 sera 1.5 veces mas que el la paga de todas las horas debajo de las 40 hora. Usa 45 horas y pago de 10.50 por hora para probar el programa( El pago debe ser 498.75) Debes usar el input para leer un string y float() para convertir el string en un numero, No te preocuper por un error de chequeo en el input de usuario, asumme que el usuario tipea los numeros adecuadamente 


hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))

#Condicional si las horas trabajas es superior a las 40
if hours > 40:
    payment = hours * rate
    extrahours = hours - 40
    payrate = rate * 0.5
    extrapayment = extrahours * payrate 
    payment = payment + extrapayment
   
else:
    payment = hours * rate


print("Pay:", payment)