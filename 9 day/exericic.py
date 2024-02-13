import random

aleatori = random.randint(1,100)

sortir = ""

while sortir.upper() != "N":
    try:
               
        jugador = int(input("Introdueix un número: "))

        if jugador > aleatori:
            print("El teu número és més gran que el de la màquina")
        elif jugador < aleatori:
            print("El teu  número és més petit que el de la màquina")
        else:
            print("Has encertat el número")
            sortir = input("Vols continuar jugant? (S/N)")

    except ValueError:
        print("Has d'introduir un número")

    
    
    
    