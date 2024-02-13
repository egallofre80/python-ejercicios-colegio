import random


for i in range(1,10):
    numero = random.randint(1,500)
    if ( numero % 2) == 0:
        print("El numero ", numero, " és parell")
    else: 
        print("El numero ", numero, " és imparell")