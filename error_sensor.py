import random

lecturas = []
lecturas_incorrectas = []

while True:

    temperatura = random.randint(10, 40)

    lectura_sensor = float(input("Introduzca la lectura del sensor: "))

    lecturas.append(lectura_sensor)

    if lectura_sensor < 10 or lectura_sensor > 40:
        lecturas_incorrectas.append(lectura_sensor)

    respuesta = input("¿Quiere continuar? (Si/No): ")

    if respuesta == "No":
        break

porcentaje_error = len(lecturas_incorrectas) / len(lecturas) * 100

print("Porcentaje de lecturas incorrectas:", porcentaje_error, "%")
