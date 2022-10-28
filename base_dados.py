#https://pandas.pydata.org/

#Relatorio de analise I
#Importando base de dados
import sys
import pandas as pd


dados = pd.read_csv('../Python_Pandas_TRATANDO_ANALISANDO_DAD0S/dados/aluguel.csv', sep=';')
type(dados)
print(dados)
print(dados.head(10))

#Informações gerais sobre a base de dados
print(dados.dtypes, '\n')
tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipo de dados'])
tipos_de_dados.columns.name = 'Variaveis'
print(tipos_de_dados, '\n')

print(dados.shape)
print(dados.shape[0])
print(dados.shape[1], '\n')

print('A base de dados apresenta {} registros (imoveis) e {} variaveis.'.format(dados.shape[0], dados.shape[1]))

