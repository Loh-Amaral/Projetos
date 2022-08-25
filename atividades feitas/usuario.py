#x = True 
#while x == True:

 #   idade = int(input('qual a sua idade'))

   # if idade < 18
  #  print("usuario não pode tirar a carteira")

   # else: 
    #print ('já pode tirar a carteira, meus parabens')




#from re import X


#x = 0

#while True:
#    if x == 17000:
#        break
 #   print(x)
 #   x = x + 1
usu=[]
sen=[]

from hashlib import sha3_224
while True:
    print("vamos criar um usuario")

    u1 = str(input("digite o nome de usuario "))
    usu.append(u1)

    s1 = str(input("digite a senha para usuario "))
    sen.append(s1)


    print(usu)
    print(sen)
  


    print("Faça Login")


    u2 = str(input("digite o nome do usuario "))

    s2 = str(input('digite a senha '))

    if u1 == u2  and s1 == s2:
            print("ACESSO LIBERADO")                                                                                                         
    else:
            print("ACESSO NEGADO")

    break
