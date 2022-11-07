import pandas as pd


data = [['Fulano', 12, 7.0, True], ['Sicrano', 15, 3.5, False], ['Beltrano', 18, 9.3, True]]
dados = pd.DataFrame(data,columns = ['Aluno', 'Idade', 'Nota', 'Aprovado'])

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.federalreserve.gov/releases/h3/current/default.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll('table')
html_file = f'<html><body>{table}</body></html>'
df = pd.read_html(html_file)

# Como a função read_html retorna uma lista de DataFrames, basta acessar as tabelas pelos índices da lista.
# Como temos três tabelas na página usamos os índices 0, 1 ou 2 para acessar os DataFrames que buscamos
df[0]

print('\n')

import pandas as pd

numeros = [i for i in range(11)]
letras = [chr(i + 65) for i in range(11)]
nome_coluna = ['N']
print(nome_coluna)

df = pd.DataFrame(data = numeros, index = letras, columns = nome_coluna)

selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
df = df[selecao]
print(df, '\n')

import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])