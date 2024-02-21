print("TIP Calculator\n")

totalFactura = float(input("¿Cuál es el importe final de la factura? "))
totalPersonas = int(input("¿Total de personas? "))
porcentaje =  int(input("Quin percentatge vols donar? 10, 12 or 15 "))

importTotalPercentage = (totalFactura*porcentaje)/100
importIndividual = (importTotalPercentage + totalFactura) / totalPersonas

print("Cada persona tiene que pagar", round(importIndividual, 2))