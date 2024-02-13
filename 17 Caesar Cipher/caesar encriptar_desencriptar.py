import encriptar

frase = input("Escriu la frase a encriptar: ")
salt = int(input("Introdueix el salt entre lletres: "))

opcio = input("Encriptor (e) o desencriptar (d): ")

#if (opcio.lower() == 'e'):
#    encriptar.xifrar(frase, salt)
#else:
#    encriptar.desxifrar(frase, salt)

encriptar.caesar(frase, salt, opcio)