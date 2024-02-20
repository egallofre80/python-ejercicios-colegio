import calculadora

try :
    operador1 = int(input("Introdueix el primer operador: "))
    operador2 = int(input("Introdueix el segon operador: "))
except ValueError:
        print("Número no válida")

calculadora.suma(operador1, operador2)
calculadora.resta(operador1, operador2)
calculadora.mult(operador1, operador2)
calculadora.division(operador1, operador2)
calculadora.exponencial(operador1,  operador2)