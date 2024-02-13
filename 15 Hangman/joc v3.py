import random

paraules = ["poma", "pera", "llimona", "taronja", "mandarina", "sindria", "melo"]
visualitzar = []

paraula = paraules[random.randint(0,6)]

print("La paraula és: ", paraula)

llargadaParaula = len(paraula) + 1

for caracter in range(1, llargadaParaula):
    visualitzar += "_"

print(' '.join(visualitzar))

finalJoc = False

while finalJoc == False:

    lletraJugador = input("Introdueix una lletra? ")

    posicio = 0
    for lletra in paraula:

        if lletraJugador== lletra:
          visualitzar[posicio] = lletra

        posicio = posicio + 1
    
    print(' '.join(visualitzar))

    if "_" not in visualitzar:
        print("Has Guanyat")
        finalJoc = True