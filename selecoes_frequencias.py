#Relatorio IV
import pandas as pd
dados = pd.read_csv('dados/aluguel_residencial.csv', sep =';')

#Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = dados['Tipo'] == 'Apartamento'
print(selecao)
n1 = dados[selecao].shape[0]
print(n1, '\n')

#Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio' )| (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
print(n2, '\n')

#Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
print(n3, '\n')

#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
print(n4, '\n')

print("Selecione somente os imóveis classificados com tipo 'Apartamento' -> {}". format(n1))

print("Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila' -> {}". format(n2))

print("Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}". format(n3))

print("Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}". format(n4))
