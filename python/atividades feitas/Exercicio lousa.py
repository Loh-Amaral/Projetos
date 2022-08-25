q=int(input('digite a quantidade de numeros que deseja digitar: '))
contador = 0
lista=[]
maior=''
menor=''

while contador < q:
    n = int(input('digite um numero: '))
    lista.append(n)
    contador += 1
    if maior == '':
        maior = n
    else:
        if n>maior:
            maior = n
    if menor =='' :
        menor = n
    else:
        if n<menor:
            menor = n

print('lista',lista)
print('numero maior ',maior)
print('numero menor ',menor)