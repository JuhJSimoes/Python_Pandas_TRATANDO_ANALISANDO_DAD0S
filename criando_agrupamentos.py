import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/aluguel.csv', sep = ';')
print(dados.head(10), '\n')

print(dados['Valor'].mean(), '\n')

'''bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]'''
print(dados['Bairro'].drop_duplicates(), '\n')

grupo_bairro = dados.groupby('Bairro')
type(grupo_bairro)
#print(grupo_bairro.groups) indices onde encontra o registro ex.: Barra da Tijuca indice 7

for bairro, data in grupo_bairro:
    print('{} -> {}'.format(bairro, data.Valor.mean()), '\n')
    
print(grupo_bairro[['Valor', 'Condominio']].mean().round(2))

print(grupo_bairro['Valor'].describe().round(2),'\n')

print(grupo_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns = {'min': 'Minimo','max': 'Maximo', 'sum': 'Soma'}))


plt.rc('figure', figsize=(20,10))

print(grupo_bairro['Valor'].std().plot.bar(color='blue'))
plt.show() #para exibir no VS Code

