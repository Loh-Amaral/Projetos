import math

a = float(input("Digite o valor de A: "))

if a == 0:
    print("Valor Invalido")
else:
    b = float(input("Digite  o valor de B: "))
    c = float(input("Digite o valor de C: "))


d1 = (b ** 2) - (4 * a * c)


if d1 < 0:
    print("A equação não possui raizes ")
else:
    r1 = (-b + (math.sqrt(d1)) / 2 * a)
    r2 = (-b - (math.sqrt(d1)) / 2 * a) 

if d1 == 0:
    print("1 Raiz real: ", r1)
else:
    print("2 raizes reais, r1: ", r1, "r2: ", r2)
