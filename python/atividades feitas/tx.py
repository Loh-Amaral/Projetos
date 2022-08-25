from urllib import request
import requests

nome=str(input('digite o seu nome: '))
response = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome.upper()}').json()
print(response)

while True:
    for i in range (0,len(response[0]['res'])):
        print(f"no periodo {response[0]['res'][i]['periodo']} tem {response[0]['res'][i]['frequencia']} nomes iguais a {nome}")
    nome=str(input('digite o seu nome: '))
    print(f"no periodo {response[0]['res'][i]['periodo']} tem {response[0]['res'][i]['frequencia']} nomes iguais a {nome}")
    
    break
