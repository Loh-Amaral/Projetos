
from distutils.log import INFO, info
import requests


nome=str(input('digite o nome de uma cidade: '))
info = requests.get(f'https://weather.contrateumdev.com.br/api/weather/city/?city={nome}').json()



temp=info['main']['temp']
min=info['main']['temp_min']
max=info['main']['temp_max']
des=info['weather'][0]['description']
im= info['main']['humidity']


print(f'A temperátura atual é de {temp} graus')
print(f'A temperátura minima é de {min} graus')
print(f'A temperátura máxima é de {max} graus')
print(f'Humidade de {im} %')
print(f'A cidade de {nome} encontrasse no momento com {des}')
