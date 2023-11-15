lecturas= int(input("¿Cuántas lecturas de temperatura tienes?"))
temp_1 = 0
temp_2 = 0
temp_3 = 0

while temp_1 < lecturas:
      temp_1 += 1
      t = float(input("Escribe la temperatura: "))
      if t >= 10 and t <= 40:
          pass
      else:
          temp_3 += 1

print("Número de lecturas fuera del rango:", temp_3)

porcentaje = (temp_3 * 100) / lecturas

print("Porcentaje de lecturas fuera del rango:",porcentaje)
