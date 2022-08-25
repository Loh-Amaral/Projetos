
while True:
    n1= float(input('digite um numero para a operação: '))
    r1= str(input('digite o operador para a operação: ' ))
    n2= float(input('digite outro numero para a operação: ')) 
    if r1 == "+":
        print(n1+n2)
    elif r1 == "-":
        print(n1-n2)
        n1= float(input('digite um numero para a operação: '))
        r1= str(input('digite o operador para a operação: ' ))
        n2= float(input('digite outro numero para a operação: '))   
    elif r1 == "*" or r1 == 'x':
        print(n1*n2)
        n1= float(input('digite um numero para a operação: '))
        r1= str(input('digite o operador para a operação: ' ))
        n2= float(input('digite outro numero para a operação: '))   
    elif r1 == '/':
        print(n1/n2)
        n1= float(input('digite um numero para a operação: '))
        r1= str(input('digite o operador para a operação: ' ))
        n2= float(input('digite outro numero para a operação: '))   
    elif r1 != '+'and r1!='-' and r1!='*'and r1!='x'and r1!='/':
        print('opção invalida')

