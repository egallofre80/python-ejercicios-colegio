numeros = [99,15,4,1,23,78,101,3,54]

num_auxiliar = 0
total_numeros = len(numeros) 
posicioInicial = 0

for posicioInicial in range(0, total_numeros):
    for num in range(posicioInicial, total_numeros ):
        if numeros[posicioInicial] > numeros[num]:
            num_auxiliar =  numeros[posicioInicial]
            numeros[posicioInicial] = numeros[num]
            numeros[num]= num_auxiliar
    
print ("La llista ordenada és:")
print(numeros)
        


