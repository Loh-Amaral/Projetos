
import random

contador = 0

pc = random.randint(1,100)
 
u = int(input('digite um numero '))
while u != pc and contador < 4:
        print('numero é maior')
        u = int(input('digite outro numero ')) 
        contador += 1
        if u > pc: 
            print('o numero é menor ')
            u = int(input('digite outro numero '))
            contador += 1
            if contador == 5:
                print('suas tentativas acabaram')
            elif u == pc:
                print("meus parabens você acertou ") 
    
print(pc)

