
nome = str(input('qual seu nome '))

while len(nome) < 3:
    print(' seu nome deve ter mais que 3 digitos')
    nome = str(input('digite o seu nome '))

idade = int(input('qual seu idade '))

while idade > 70 or idade < 0:
    print('sua idade deve estar entre 0 e 70 anos ')
    idade = int(input('qual sua idade '))

salario = float(input('qual seu salário '))

while salario <= 0:
    print(input('seu salário tem que ser maior que 0'))
    salario = float(input('qual seu salário: '))

sexo = str(input('qual seu genero '))

while sexo != 'm' and sexo != 'f':
    print('genero invalido')
    sexo = str(input(' qual seu genero'))


estado = str(input('qual seu estado civil '))

while estado != 's' and estado != 'c' and estado != "v":
    print('estado civil invalido ')
    estado= str(input('digite o estado civil'))
