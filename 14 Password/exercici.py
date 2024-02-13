import random

lletres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbols = ['!', '#', '$', '%', '&', '(',')','/','*','+']

num_lletres = int(input("Quantes lletres vols? "))
num_numeros = int(input("Quants números vols? "))
num_simbols = int(input("Quants símbols vols? "))

password = ""

for char in range (1, num_lletres + 1):
    password = password + random.choice(lletres)

for sim in range(1, num_simbols + 1):
    password = password + random.choice(simbols)

for num in range(1, num_numeros + 1):
    password = password + random.choice(numeros)    

print("El password és: ", password )            