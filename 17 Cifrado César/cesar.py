letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]

def encriptar(frase, salto):
    
    textoCifrado = ""

    for letra in frase:
            posicionLetra = letras.index(letra)
            nuevaPosicion = posicionLetra + salto
            textoCifrado = textoCifrado + letras[nuevaPosicion]
    
    print(f"El texto cifrado es {textoCifrado}")