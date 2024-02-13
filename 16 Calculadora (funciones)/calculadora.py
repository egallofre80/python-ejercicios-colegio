def suma(num1, num2):
    resultat = num1 + num2
    print(f"La suma és {resultat}")

def resta(num1 , num2):
    resultat = num1 - num2
    print(f"La resta és {resultat}")

def mult(num1, num2):
    resultat = num1 * num2
    print(f"La multiplicació és {resultat}")

def divisio(num1, num2):
    if (num2 > 0):
        resultat = num1 / num2
        print(f"La divisió és {resultat}")
    else:
        print("NO es pot fer la divisió")


####################

operador1 = int(input("Introdueix el primer operador: "))
operador2 = int(input("Introdueix el segon operador: "))

suma(operador1, operador2)
resta(operador1, operador2)
mult(operador1, operador2)
divisio(operador1, operador2)
