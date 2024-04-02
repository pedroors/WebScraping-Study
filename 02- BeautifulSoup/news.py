import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

# Transformar o conteúdo da página para o formato do BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

# HTML da notícia / Conteúdo da página em HTML
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Titulo da notícia
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

# Subtitulo da notícia
subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})

print('Titulo:', titulo.text)
print('Subtitulo:', subtitulo.text)