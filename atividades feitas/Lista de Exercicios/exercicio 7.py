n1 =int(input('digite um numero'))
n2 =int(input('digite o segundo numero'))
n3 =int(input('digite o terceiro numero'))

if n1 > n2 and n1 > n3:
    print('o primeiro numero é o maior')
elif n2 > n1 and n2 > n3:
    print('o segundo numero é o maior')
elif n3 > n1 and n3 > n2:
    print('o terceiro numero é o maior')
if n1< n2 and n1 < n3:
    print('o primeiro numero é o menor ')
elif n2< n1 and n2 < n3:
    print('o segundo numero é o menor ')
elif n3< n2 and n3 < n1:
    print('o terceiro numero é o menor ')