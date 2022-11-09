import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]

s = pd.Series(data)
print (s, '\n')

print(s.fillna(0), '\n')

print(s.fillna(method = 'ffill'), '\n') #pega o ultimo valor valido e associa ao em branco - de cima para baixo

print(s.fillna(method = 'bfill'), '\n') #pega o ultimo valor valido e associa ao em branco - de baixo para cima

print(s.fillna(s.mean()), '\n') #completa com a media dos valores

print(s.fillna(method = 'ffill', limit = 1), '\n') #completa apenas 1x com o valor anterior

s1 = s.fillna(method = 'ffill', limit = 1)

print(s1.fillna(method = 'bfill', limit = 1))


