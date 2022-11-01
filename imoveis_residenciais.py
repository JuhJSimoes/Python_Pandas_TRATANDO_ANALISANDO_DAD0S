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