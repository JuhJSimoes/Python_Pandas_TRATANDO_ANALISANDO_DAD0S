import pandas as pd


data = [['Fulano', 12, 7.0, True], ['Sicrano', 15, 3.5, False], ['Beltrano', 18, 9.3, True]]
dados = pd.DataFrame(data,columns = ['Aluno', 'Idade', 'Nota', 'Aprovado'])

print(dados)