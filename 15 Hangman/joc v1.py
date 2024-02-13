import random

paraules = ["poma", "pera", "llimona", "taronja", "mandarina", "sindria", "melo"]

paraula = paraules[random.randint(0,6)]

print("La paraula és: ", paraula)

lletraJugador = input("Introdueix una lletra? ")

for lletra in paraula:
    if lletraJugador== lletra:
        print("Correcte")
    else:
        print("Incorrecte")