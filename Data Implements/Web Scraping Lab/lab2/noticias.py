import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.google.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tag_div = soup.find('div', class_='TDaRVd')
tag_button = tag_div.find_all('button')

noticias = []

for noticia in tag_div.find_all('button'):
    noticia = noticia.get('aria-label').replace('More - ', '')
    noticias.append(noticia)

df_top5 = pd.DataFrame(noticias)
df_top5.columns = ['Top 5 noticias']

for titulo in df_top5['Top 5 noticias'].head(5):
    print(titulo)

