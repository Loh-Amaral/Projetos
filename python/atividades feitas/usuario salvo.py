
print('vamos criar um usuario')
usuario = open('usuario.txt', 'a')
usuario.write(f"{input('digite o nome de usuario ')}\n")
senha = open('senha.txt', 'a')
senha.write(f"{input('digite a senha para usuario ')}\n")

  
  