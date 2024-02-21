import calculadora

try :
    operador1 = int(input("Introduce el primer operador: "))
    operador2 = int(input("Introduce el segundo operador: "))

    calculadora.suma(operador1, operador2)
    calculadora.resta(operador1, operador2)
    calculadora.mult(operador1, operador2)
    calculadora.division(operador1, operador2)
    calculadora.exponencial(operador1,  operador2)
except ValueError:
        print("Número no válido")

