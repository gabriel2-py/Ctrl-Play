import requests
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/start/esport/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')


lista = ['lol','valont','fifa','fortinite']


for paragrafo in  soup.find_all('body'):
    for palavra in lista:
        for paragrafo_str in paragrafo.stripped_strings:
            if palavra.upper() in str (paragrafo_str).upper():
                print('NOTÍCIA SOBRE:', palavra.upper(), '\n', paragrafo_str,'\n')
                break