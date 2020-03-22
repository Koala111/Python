import pandas as pd
data = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(data)
print(data.values)
print(data.index)
print(len(data)) #获取长度
print(data[['a','c']])
print(data.value_counts())
print(data.isnull())
