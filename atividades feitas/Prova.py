
n1 = int(input('digite um numero do seu CPF, em sequencia: '))
n2 = int(input('digite um numero do seu CPF, em sequencia: '))
n3 = int(input('digite um numero do seu CPF, em sequencia: '))
n4 = int(input('digite um numero do seu CPF, em sequencia: '))
n5 = int(input('digite um numero do seu CPF, em sequencia: '))
n6 = int(input('digite um numero do seu CPF, em sequencia: '))
n7 = int(input('digite um numero do seu CPF, em sequencia: '))
n8 = int(input('digite um numero do seu CPF, em sequencia: '))
n9 = int(input('digite um numero do seu CPF, em sequencia: '))
n10 = int(input('digite um numero do seu CPF, em sequencia: '))
n11 = int(input('digite um numero do seu CPF, em sequencia: '))
cpf=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
print('o CPF Inserido foi: ',cpf)

if n1 == n3 :
    print('CPF INVALIDO')
    n1 = int(input('digite um numero do seu CPF, em sequencia: '))
    n2 = int(input('digite um numero do seu CPF, em sequencia: '))
    n3 = int(input('digite um numero do seu CPF, em sequencia: '))
    n4 = int(input('digite um numero do seu CPF, em sequencia: '))
    n5 = int(input('digite um numero do seu CPF, em sequencia: '))
    n6 = int(input('digite um numero do seu CPF, em sequencia: '))
    n7 = int(input('digite um numero do seu CPF, em sequencia: '))
    n8 = int(input('digite um numero do seu CPF, em sequencia: '))
    n9 = int(input('digite um numero do seu CPF, em sequencia: '))
    n10 = int(input('digite um numero do seu CPF, em sequencia: '))
    n11 = int(input('digite um numero do seu CPF, em sequencia: '))

else: 
    vl= (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)
    r=((vl*10)%11)
    if r == 10:
        r = 0
    print('o penultimo nurero do CPF tem que ser: ',r)

vl2= (n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (n10 * 2)
r2=((vl2*10)%11)
if r2 == 10:
    r2 = 0
print('o ultimo numero do cpf tem que ser: ',r2)

if r == n10 and r2 == n11:
    print('o CPF: ',cpf,"é valido")

else:
    print("o Cpf: ", cpf,'é invalido')
