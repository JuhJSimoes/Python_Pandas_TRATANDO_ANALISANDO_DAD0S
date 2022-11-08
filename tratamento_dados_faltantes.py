import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep=';')

print(dados.head(10))

print(dados.isnull())

print(dados.notnull())

print(dados.info())

print(dados[dados['Valor'].isnull()], '\n')

A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace=True)
B = dados.shape[0]
print(A - B, '\n')

print(dados[dados['Valor'].isnull()], '\n')

print(dados[dados['Condominio'].isnull()].shape[0], '\n')

selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())

A = dados.shape[0]
dados = dados[~selecao] #o til ~ Inverte a series. Ex.: falso se torna verdadeiro e vice versa
B = dados.shape[0]
print(A - B, '\n')

dados = dados.fillna({'Condominio': 0, 'IPTU': 0}) #atribui o valor por coluna

dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)


