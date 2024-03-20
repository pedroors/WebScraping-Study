import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})


for noticia in noticias:

    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    #print('Titulo da matéria:\n', titulo.text)

    subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})

    if(subtitulo):
        # print('Subtitulo da matéria:\n', subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', ''])


news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

news.to_excel('Noticias.xlsx', index=False)

#print(news)