from re import I


Lista = [1,3,7,10,22,45,73,265,41,17]
pares = []
impares = []

for i in Lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('lista inicial',Lista )
print('lista de numeros pares ', pares)
print('lista de numeros impares', impares)