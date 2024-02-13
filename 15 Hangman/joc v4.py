import random

paraules = ["poma", "pera", "llimona", "taronja", "mandarina", "sindria", "melo"]
visualitzar = []

ninot = ['''
            +----+
            |    
            |
            |
            |
          =====  

         ''',
         '''
            +----+
            |    O
            |
            |
            |
          =====  
         ''',
         '''
            +----+
            |    O
            |   /    
            |
            |
          =====  
        ''' ,
         '''
            +----+
            |     O
            |   / |   
            |
            |
          =====  
        '''  ,
         '''
            +----+
            |     O
            |   / | \  
            |
            |
          =====  
        ''' ,
         '''
            +----+
            |     O
            |   / | \  
            |    / 
            |
          =====  
        ''',
        '''
            +----+
            |     O
            |   / | \  
            |    / _
            |
          =====  
        '''              
          ]



paraula = paraules[random.randint(0,6)]

print("La paraula és: ", paraula)

llargadaParaula = len(paraula) + 1

for caracter in range(1, llargadaParaula):
    visualitzar += "_"

print(' '.join(visualitzar))

finalJoc = False
vides = 0

while finalJoc == False:

    lletraJugador = input("\nIntrodueix una lletra? ")

    posicio = 0
    for lletra in paraula:

        if lletraJugador== lletra:
          visualitzar[posicio] = lletra

        posicio = posicio + 1

    print(' '.join(visualitzar))

    if lletraJugador not in paraula:
        vides = vides + 1
        if vides == 6:
            print("\nHas perdut")
            finalJoc = True
    
    if "_" not in visualitzar:
        print("\nHas Guanyat")
        finalJoc = True

    print(ninot[vides])