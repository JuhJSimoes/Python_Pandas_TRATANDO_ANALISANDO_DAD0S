import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})
print(dados.head(10), '\n')

dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
print(dados.head(10), '\n')

dados['Valor m2'] = dados['Valor'] / dados['Area']
print(dados.head(10), '\n')

dados['Valor m2'] = dados['Valor m2'].round(2)
print(dados.head(10), '\n')

dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)
print(dados.head(10), '\n')

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento') #permite que aplique a função a cada registro do data frame
print(dados, '\n')

dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
print(dados_aux.head(10),'\n')

del dados_aux['Valor Bruto']
print(dados_aux.head(10),'\n')

dados_aux.pop('Valor Bruto m2')
print(dados_aux.head(10),'\n')

dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)
print(dados.head(10),'\n')

dados.to_csv('dados/aluguel_residencial.csv', sep =';', index = False)