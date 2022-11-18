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
'''dados_new.boxplot(['Valor'])


dados.hist(['Valor'])
dados_new.hist(['Valor'])

#plt.show()'''

dados.boxplot(['Valor'], by = ['Tipo'])
#plt.show()

grupo_tipo = dados.groupby('Tipo')['Valor']
#print(type(grupo_tipo))

print(grupo_tipo.groups, '\n')

Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
print(Q1)
print(Q3)
print(limite_inferior)
print(limite_superior)
print(limite_superior['Apartamento'],'\n')

dados_new =pd.DataFrame()

for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

print(dados_new.head(10))
dados_new.boxplot(['Valor'], by = ['Tipo'])
plt.show()

dados_new.to_csv('dados/aluguel_residencial_sem_outliers.csv', sep=';', index=False)








