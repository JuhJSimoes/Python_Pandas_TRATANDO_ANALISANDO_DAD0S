import pandas as pd

#'l1 l2 l3 l4'.split() 

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
print(df, '\n')

print(df[['c3', 'c1']], '\n') #Seleção por coluna

print(df[1:2], '\n') #Seleção por linha - index

print(df[1:][['c3', 'c1']], '\n') #Seleção por linha e coluna

print(df.loc['l3'], '\n') #Seleção por linha - rotulo da linha

print(df.loc['l2', 'c3'], '\n') #Seleção por rotulo da linha e coluna

print(df.iloc[1,2], '\n') #Seleção por index da linha e coluna