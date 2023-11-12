def detecta_alexa(texto):
    palabras = texto.split()
    return palabras.count("Alexa")

texto = input("Introduce un texto: ")

numero_alexas = detecta_alexa(texto)
if numero_alexas == 1:
   print("¿Como puedo ayudarte?")
    
elif numero_alexas > 1:
    print("Tranquilo, solo di mi nombre una vez")
