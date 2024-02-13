fruites = []
usuari = ""

while usuari.upper() !='S':
    usuari = input("Introdueix una fruita: ")
    if usuari.upper() != 'S':
        fruites.append(usuari)

print("Les fruites introduïdes són: ")
for fruita in fruites:
    print(fruita)