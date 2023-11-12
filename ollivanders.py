import random

clientes = []
varitas = []

while True:
    numero = random.randint(1, 100)
    if numero < 50:
        varita = random.randint(1, 4)
        numero_cliente = input("Introduzca el número del cliente: ")
        tipo_varita = input("Introduzca el tipo de varita (Sauco, Espino, Sauce, Acebo): ")

        clientes.append(numero_cliente)
        varitas.append(tipo_varita)
        
    else:
        continue
    respuesta = input("¿Quiere continuar? (Si/No): ")

    if respuesta == "No":
        break
        
print("Clientes que entraron a la tienda:", clientes)
print("Varitas vendidas:", varitas)

varitas_sauco = varitas.count(1)
varitas_espino = varitas.count(2)
varitas_sauce = varitas.count(3)
varitas_acebo = varitas.count(4)

       
print("Número de varitas de Saúco:", varitas_sauco)
print("Número de varitas de Espino:", varitas_espino)
print("Número de varitas de Sauce:", varitas_sauce)
print("Número de varitas de Acebo:", varitas_acebo)
