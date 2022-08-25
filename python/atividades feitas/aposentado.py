x = str(input("qual é o seu gênero, f ou m ")).lower()


if x == "f":
    print("você pode se aposentar com 60 anos")
elif x == "m":
    print('você pode se aposentar com 65 anos')
else:
    print("opção invalida")