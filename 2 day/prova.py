print("TIP Calculator\n")

totalFactura = float(input("Quin és l'import final de la factura? "))
totalPersones = int(input("Total de persones? "))
percentatge =  int(input("Quin percentatge vols donar? 10, 12 or 15 "))

importTotalPercentage = (totalFactura*percentatge)/100
importIndividual = (importTotalPercentage + totalFactura) / totalPersones

print("Cada persona ha de pagar", round(importIndividual, 2))