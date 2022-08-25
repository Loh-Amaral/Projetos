#a = #10
#b = 2#
#
#print(a+b)
##print(a-b)
#print(a*b)
###print(a/b)
#print(a%b)
##print(a//b)
#print(a**b#


#n1 = float(input('digite a area do quadrado '))

#print('a area do quadrado é ',(n1**2))
#print('o dobro da area do quadrado é ',((n1**2)*2))

#manipulação de string

#nome =  'esTou nO joVem prOGRAmador'

#print(nome)
#maiusculo
#print(nome.upper())
#minusculo
#print(nome.lower())
#algumas letras maiusculas
#print(nome.title())
# primeira letra maiuscula
#print(nome.capitalize())
#tirar espaços
#print(nome.strip())

#numero de caracter na frase
#print(len(nome))



s1 = float(input('digite o valor do seu salário por hora '))
s2 = float(input('digite as horas trabalhadas '))

print('seu salário bruto é',(s1*s2))
print('o desconto do inss (11%) ',(11/100*(s1*s2)))
print("o desconto de inss(8%)é ",((8/100*(s1*s2))))
print("o desconto de sindicato (5%)é ",((5/100*(s1*s2))))
print("seu salário liquido é ",((s2*s1)-(((11/100*(s1*s2))+(8/100*(s1*s2))+(5/100*(s1*s2))))))