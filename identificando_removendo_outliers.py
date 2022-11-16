import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(14,6))

dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')



print(dados[dados['Valor']>= 500000],'\n')
valor = dados['Valor']
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]

#dados.boxplot(['Valor'])
dados_new.boxplot(['Valor'])


dados.hist(['Valor'])
dados_new.hist(['Valor'])

plt.show()
