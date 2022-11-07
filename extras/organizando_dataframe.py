import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]
print(list('321'), '\n')

df = pd.DataFrame(data, list('321'), list('ZYX'))
print(df, '\n')

df.sort_index(inplace= True)
print(df, '\n')

df.sort_index(inplace= True, axis = 1)
print(df, '\n')

df.sort_values(by='X', inplace=True)
print(df, '\n')

df.sort_values(by='3', axis = 1, inplace=True)
print(df, '\n')
