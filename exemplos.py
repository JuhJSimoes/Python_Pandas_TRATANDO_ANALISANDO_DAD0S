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

selecao = alunos['Aprovado'] == True
aprovados = alunos[selecao]
print(aprovados, '\n')

selecao = (alunos.Aprovado == True) & (alunos.Sexo == 'F')
aprovadas = alunos[selecao]
print(aprovadas, '\n')

selecao = ((alunos.Idade > 10) & (alunos.Idade < 20)) | (alunos.Idade >= 40)
print(alunos[selecao], '\n')

imoveis = pd.DataFrame([['Apartamento', None, 970, 68], 
                        ['Apartamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Apartamento', None, 1010, 170], 
                        ['Apartamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Apartamento', 2000, 878, None], 
                        ['Apartamento', 1550, None, 228], 
                        ['Apartamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])


imoveis.dropna(subset = ['Valor'], inplace = True)
print(imoveis)

selecao = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
imoveis = imoveis[selecao]
print(imoveis)

imoveis = imoveis.fillna({'Condominio': 0, 'IPTU': 0})
print(imoveis)

imoveis.index = range(imoveis.shape[0])  # type: ignore
print(imoveis, '\n')

atletas = pd.DataFrame([['Marcos', 9.62], ['Pedro', None], ['João', 9.69], 
                        ['Beto', 9.72], ['Sandro', None], ['Denis', 9.69], 
                        ['Ary', None], ['Carlos', 9.74]], 
                        columns = ['Corredor', 'Melhor Tempo'])
print(atletas, '\n')

import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas'])

alunos['Notas-Média(Notas)'] = alunos.Notas - alunos.Notas.mean()
print(alunos, '\n')

alunos['Notas-Média(Notas)'] = alunos['Notas'].apply(lambda x: x - alunos['Notas'].mean())
print(alunos, '\n')

alunos['Faixa Etária'] = alunos['Idade'].apply(lambda x: 'Menor que 20 anos' if x < 20 
        else ('Entre 20 e 40 anos' if (x >= 20 and x <= 40) 
            else 'Maior que 40 anos'))
print(alunos, '\n')
    

