numeros = []
sortir = ""

while sortir.upper() !='N':
    try:
        numeroUsuari = int(input("Introdueix un número: "))
        numeros.append(numeroUsuari)
        sortir = input("Vols continuar introduint números? (S/N)")
    except ValueError:
        print("Has d'introduir un número")


numeros.sort()

print("Els números introduits són: ")
for num in numeros:
    print(num)