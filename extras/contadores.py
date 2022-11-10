import pandas as pd

s = pd.Series(list('asasadasasdasdfweasassdasderegvdf'))
print(s)

print(s.unique())

print(s.value_counts())

dados = pd.read_csv('dados/aluguel.csv', sep = ';')
print(dados.Tipo.unique(),'\n')
print(dados.Tipo.value_counts(),'\n')
