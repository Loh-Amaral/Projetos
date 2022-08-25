contador = 0

n1= int(input('digite quantas notas você deseja colocar: '))
media = 0
while contador !=n1:
    r= float(input('digite sua nota '))
    contador += 1
    media += r
print (media/n1)    
