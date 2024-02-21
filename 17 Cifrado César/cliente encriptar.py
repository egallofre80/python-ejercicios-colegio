import cesar

frase = input("Escribe la frase a encriptar: ")

try:

    salto = int(input("Introduce el salto entre letras: "))
    cesar.encriptar(frase, salto)

except ValueError:
    print("Error al introducir el valor del salto entre letras")