# > EXEMPLO
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

url_base = 'https://www.magazineluiza.com.br/busca/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={
    'class': 'sc-eBMEME uPWog sc-cDnByv dgyHCD sc-cDnByv dgyHCD'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'sc-fvwjDU fbccdO'})
    link = produto.find('a', attrs={'class': 'sc-eBMEME uPWog sc-cDnByv dgyHCD sc-cDnByv dgyHCD'})


    print(produto.prettify())
    print('Título do produto:', titulo.text)
    print('Link do produto:', link['href'])

    print('\n\n')
    break



