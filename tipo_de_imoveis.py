#Relatorio de analises
#Tipos de imoveis

import pandas as pd

dados = pd.read_csv('../Python_Pandas_TRATANDO_ANALISANDO_DAD0S/dados/aluguel.csv', sep=';')
dados.head(10)

print(dados['Tipo'], '\n')

tipo_de_imovel = dados['Tipo']
print(tipo_de_imovel, '\n')
tipo_de_imovel.drop_duplicates()
tipo_de_imovel.drop_duplicates(inplace = True)

print(tipo_de_imovel, '\n')

#Organizando a visualização

tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
print(tipo_de_imovel)


print(tipo_de_imovel.index)
print(tipo_de_imovel.shape[0])
print(range(tipo_de_imovel.shape[0]))
for i in range(tipo_de_imovel.shape[0]):
    print(i)
    
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
print(tipo_de_imovel, '\n')

tipo_de_imovel.columns.name = 'ID'
print(tipo_de_imovel)