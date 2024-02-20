def suma(num1, num2):
    resultado = num1 + num2
    print(f"La suma es {resultado}")

def resta(num1 , num2):
    resultado = num1 - num2
    print(f"La resta es {resultado}")

def mult(num1, num2):
    resultado = num1 * num2
    print(f"La multiplicación es {resultado}")

def division(num1, num2):
    if (num2 > 0):
        resultado = num1 / num2
        print(f"La división es {resultado}")
    else:
        print("No se puede realizar la división")

def exponencial(base, exp):
    resultado = base ** exp;
    print(f"{base} elevado a {exp} es: {resultado}")