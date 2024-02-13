lletres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]


def xifrar(frase, salt):
    
    textXifrat = ""

    for lletra in frase:
            posicioLletra = lletres.index(lletra)
            novaPosicio = posicioLletra + salt
            textXifrat = textXifrat + lletres[novaPosicio]
    
    print(f"El text xifrat és {textXifrat}")

def desxifrar(frase, salt):
    textDesxifrat = ""

    for lletra in frase:
            posicioLletra = lletres.index(lletra)
            novaPosicio = posicioLletra - salt
            textDesxifrat = textDesxifrat + lletres[novaPosicio]
    print(f"El text desxifrat és {textDesxifrat}")

def caesar(frase, salt, metode):
    textFinal = ""

    for lletra in frase:
        if lletra in lletres:
            posicioLletra = lletres.index(lletra)
        
            if (metode.lower() == 'e'):
                novaPosicio = posicioLletra + salt
            else:
                novaPosicio = posicioLletra - salt

            textFinal = textFinal + lletres[novaPosicio]
        else:
             textFinal = textFinal + lletra

    print(f"El text és {textFinal}")