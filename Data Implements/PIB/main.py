import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

df_table = pd.read_html(url)
df = df_table[3]

# substituindo as descrições das colunas por numeros
df.columns = range(df.shape[1])

# Retire colunas com índice 0 e 2 (nome do país e valor do PIB citado pelo FMI)
df = df[[0,2]]

# Mantenha as linhas com indice 1 a 10, indicando as top 10 economias do mundo
df = df.iloc[1:11,:]

# Atribuir nomes de colunas como "país" e "PIB (milhões de dólares)"
df.columns = ['Country','GDP (Million USD)']

# Alterando o tipo de dados para inteiro com astype
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Formatando para bilhões
df['GDP (Billion USD)'] = np.round(df['GDP (Million USD)'].map(lambda x: float(x)/1000), 2)

df = df.sort_values(by='GDP (Billion USD)', ascending=False)

print(df)

