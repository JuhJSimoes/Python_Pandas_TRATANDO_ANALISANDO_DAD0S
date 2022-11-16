import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep = ';')
print(dados.head(10))

#Contar os quartos com 1 e 2 - quartos / 3 e 4 / 5 e 6/ 7 ou mais est

classes = [0,2, 4, 6, 100]

quartos = pd.cut(dados['Quartos'], classes)
print(quartos)
print(pd.value_counts(quartos), '\n')

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou quartos ou mais']
quartos = pd.cut(dados['Quartos'], classes, labels=labels)
print(pd.value_counts(quartos),'\n')

quartos = pd.cut(dados['Quartos'], classes, labels=labels, include_lowest=True)
print(pd.value_counts(quartos),'\n')