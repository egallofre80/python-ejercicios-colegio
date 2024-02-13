lletres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
#lletres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encriptar(frase, salt):
    
    textXifrat = ""

    for lletra in frase:
        #if lletra != " ":
            posicioLletra = lletres.index(lletra)
            novaPosicio = posicioLletra + salt
            textXifrat = textXifrat + lletres[novaPosicio]
        #else:
        #    textXifrat = textXifrat + "%"
    
    print(f"El text xifrat és {textXifrat}")


frase = input("Escriu la frase a encriptar: ")
salt = int(input("Introdueix el salt entre lletres: "))

encriptar(frase, salt)