cc = 0
ac = 0
pc = 0
nc = 1
c = True

while c != 0:
    print("\nCliente n° ", nc)
    c = int(input("Digite o código: "))
    if c == 0:
        break
    else:
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        cc=[c]
        ac=[altura,altura,altura]
        pc=[peso,peso,peso]
        nc += 1  
cod_magro = pc.index(min(peso_clientes))
cod_gordo = pc.index(max(peso_clientes))
cod_alto = ac.index(max(altura_clientes))
cod_baixo = ac.index(min(altura_clientes))

print("\n" * 5)
print((pc,"Código do mais magro: ", cc))
print((pc,"Código do mais gordo: ", cc))
print((ac,"Código do mais alto: ", cc))
print((ac,"Código do mais baixo: ", cc))
print("Média de altura: ", sum(ac) / len(ac))
print("Média de peso: ", sum(pc) / len(pc))