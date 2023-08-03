#Escribe un prograba para mostrar el usuario para hora y pago por hora usando el input para computar el pago. Paga debe ser el salario normal por horas hasta 40 y medio tiempo por el salario por todas las horas trabajadas por encima de las 40 horas, Pon la logica para hacer los calculos de pago en una funcion llamada computepay() y usa la funcion para hacer los calculos. La funcion debe retornar un valor, Usa 45 horas y el salario de 10.50 por hora para probar el programa (la paga debe ser 498.75). Debes usar el input para leer un string y float() para convertir el string a un numero. NO te preocupes por error de chequeo a menos que quieras - puedes asumir que el usuario tipea numeros propiamente. No llames la variable sum o uses la funcion sum()

def computepay(hours, rate):
    hour = float(hours)
    rt = float(rate)

    pay = hour * rt

    if hour > 40:
        extrapay = (hour - 40) * (rt * 0.5)
        pay = pay + extrapay
    
    return pay

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
p = computepay(hrs, rte)
print("Pay", p)