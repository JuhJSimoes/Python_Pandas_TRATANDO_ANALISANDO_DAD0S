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