import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

#Transformar o conteúdo da página em HTML
site = BeautifulSoup(content, 'html.parser')

#HTML da noticia / Conteúdo da página em HTML
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#Titulo da noticia em HTML
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

#Subtitulo da noticia
subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})

print('Titulo:', titulo.text)
print('Subtitulo:', subtitulo.text)
