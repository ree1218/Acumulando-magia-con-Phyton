asistente = input("Escribe el nombre: ")
x = asistente.split()
repeticion_alexa = x.count("Alexa")

if repeticion_alexa == 1:
    print("Dime cómo puedo ayudarte?")
elif repeticion_alexa > 1:
    print("¡Tranquilo, solo di mi nombre una vez!")
