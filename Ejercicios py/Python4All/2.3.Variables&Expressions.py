#Escribe un programa para mostrar el usuario por horas y pago por hora, usando un input para computar el saladio. Usa 35 horas y un salario de 2.75 por hora para probar el programa (La paga debe ser 96.25). Debes usar el input para leer un string un float() para convertir el string en un numero. No te preocupes sobre un error de chequeo o mala data de usuario

#Recibir un str en un input y cambiarlo a numero con float()
hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

#Calcular las horas trabajadas multiplicando con la paga
pay = hours * rate 
print("Pay:", pay)