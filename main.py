import random

cables = ["verde", "azul", "rojo", "morado", "amarillo", "naranja"]
aleatorio = random.choice(cables)

print (aleatorio)

cuenta = (3)
eleccion = input(" En la habitacion hay una bomba con 6 cables, uno de cada color (verde, azul, rojo, morado, amarillo y naranja), tienes 3 oportunidades para cortar el que desactiva la bomba. Cual decides cortar? ")


while eleccion != aleatorio and cuenta > 0:
    print (f"Ese cable no era el que desctivava la bomba!, te quedan {cuenta - 1} intentos")
    eleccion2 = input("Elige otro cable")
    break

if cuenta == 0:
    print("La bomba ha explotado! :(")

if eleccion == aleatorio or eleccion2 == aleatorio:
    print("Has desactivado la bomba! Enhorabuena")

