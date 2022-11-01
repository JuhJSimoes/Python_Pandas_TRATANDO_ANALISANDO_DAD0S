import pandas as pd


#Series

data = [1, 2, 3, 4, 5]
s = pd.Series(data)
print(s, '\n')

index = ['Linha ' + str(i) for i in range(5)]
print(index, '\n')

s = pd.Series(data = data, index=index)
print(s, '\n')

data = {'Linha ' + str(i): i + 1 for i in range(5)}
print(data)

s = pd.Series(data)

print(data, '\n')

s1 = s + 2
print(s1, '\n')

s2 = s + s1 
print(s2, '\n')

#DataFrame

data = [[1,2,3], [4,5,6], [7,8,9]]
print(data, '\n')

df1 = pd.DataFrame(data = data)
print(df1, '\n')

index = ['Linha ' + str(i) for i in range(3)]
print(index, '\n')
df1 = pd.DataFrame(data = data, index = index)
print(df1, '\n')

columns = ['Coluna ' + str(i) for i in range(3)]
print(columns, '\n')

df1 = pd.DataFrame(data = data, index = index, columns = columns)
print(df1,'\n')

data = {'Coluna 0': {'Linha 0': 1, 'Linha 1': 4, 'Linha 2': 7},
        'Coluna 1': {'Linha 0': 2, 'Linha 1': 5, 'Linha 2': 8},
        'Coluna 2': {'Linha 0': 3, 'Linha 1': 6, 'Linha 2': 9}}
df2 = pd.DataFrame(data)
print(df2, '\n')

data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)]
df3 = pd.DataFrame(data = data, index = index, columns = columns)
print(df3, '\n')

df1[df1 > 0] = 'A'
print(df1, '\n')

df2[df2 > 0] = 'B'
print(df2, '\n')

df3[df3 > 0] = 'C'
print(df3, '\n')

df4 = pd.concat([df1, df2, df3])
print(df4, '\n')

df4 = pd.concat([df1, df2, df3], axis = 1)
print(df4, '\n')


