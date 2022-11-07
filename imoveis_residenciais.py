#Relatorio de analise III
#Imoveis residenciais

import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep = ';')
print(dados.head(10), '\n')

print(list(dados['Tipo'].drop_duplicates()))

#residencial = ['Quitinete', 'Casa', 'Conjunto Comercial/Sala', 'Apartamento', 'Casa de Condomínio', 'Prédio Inteiro',
#'Flat', 'Loja/Salão', 'Galpão/Depósito/Armazém', 'Casa Comercial', 'Casa de Vila', 'Terreno Padrão', 'Box/Garagem',
#'Loft' 'Loja Shopping/ Ct Comercial', 'Chácara', 'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 'Studio', 'Hotel', 'Indústria']

residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
dados['Tipo'].isin(residencial).head(10)
selecao = dados['Tipo'].isin(residencial)
print(selecao, '\n')

dados_residencial = dados[selecao]
print(dados_residencial, '\n')

print(list(dados_residencial['Tipo'].drop_duplicates()))

print(dados_residencial.shape[0], '\n')

dados_residencial.index = range(dados_residencial.shape[0])

print(dados_residencial, '\n')

#Exportando a Base de dados

dados_residencial.to_csv('dados/aluguel_residencial.csv', sep =';')
dados_residencial_2 = pd.read_csv('./dados/aluguel_residencial.csv', sep =';')
print(dados_residencial_2, '\n')

dados_residencial.to_csv('dados/aluguel_residencial.csv', sep =';', index = False)
dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep =';')
print(dados_residencial_2, '\n')


